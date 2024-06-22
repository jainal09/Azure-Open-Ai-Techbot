import asyncio
import json

import openai
import streamlit as st
from openai import AsyncAzureOpenAI

from src.tech_bot.configs import (
    API_KEY,
    API_VERSION,
    AZURE_DEPLOYMENT,
    AZURE_ENDPOINT,
    OAI_MODEL,
)
from src.tech_bot.utils import num_tokens_from_messages

st.title(f"Azure Open AI: GPT 4o Tech Bot 🤖")


async def get_response():
    try:
        response = await client.chat.completions.create(
            model=AZURE_DEPLOYMENT,
            messages=st.session_state.messages,
            stream=True,
            temperature=0.7,
        )  # type: ignore
    except openai.BadRequestError:
        st.error(
            "The response was filtered due to the prompt triggering Azure OpenAI's \
                  content management policy. Please modify your prompt and retry."
        )
        return
    full_response = ""
    async for chunk in response:
        data = json.loads(chunk.model_dump_json(indent=2))

        if len(data["choices"]) > 0:
            if data["choices"][0]["delta"]["content"]:
                full_response += data["choices"][0]["delta"]["content"]
            if full_response:
                message_placeholder.markdown(full_response + "▌")
    message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})


client = AsyncAzureOpenAI(
    api_key=API_KEY,
    azure_endpoint=AZURE_ENDPOINT,
    api_version=API_VERSION,
    azure_deployment=AZURE_DEPLOYMENT,
)

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = OAI_MODEL

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

st.session_state.messages.extend(
    [
        {
            "role": "system",
            "content": "You are an expert algorithm specialized in technology, \
              designed to answer questions accurately and concisely.",
        },
        {
            "role": "system",
            "content": "Answer questions using only the information contained in the \
            following technology context. Do not provide information outside of the \
            context.",
        },
        {
            "role": "system",
            "content": "Only answer questions \
            related to technology. If a question is not related to technology, \
            respond with 'I can only answer questions related to technology.'",
        },
        {
            "role": "system",
            "content": "There is A slight room of liberty to allow answering to \
            questions that still follow under the category of technology, but can be \
            less technical and revolves around technology, but not directly to technology",
        },
        {
            "role": "system",
            "content": "you are free to answer, salutations in whatever manner you like'",
        },
    ]
)

if prompt := st.chat_input("What is up?"):

    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        asyncio.run(get_response())

# Use st.markdown with inline HTML styling to change text color
st.markdown(
    f"<span style='color:red'>Total tokens used till now in conversation (your input + \
    model's output): {num_tokens_from_messages(st.session_state.messages, OAI_MODEL)}\
        </span>",
    unsafe_allow_html=True,
)
