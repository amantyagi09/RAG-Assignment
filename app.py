import streamlit as st
from rag import ask_rag  # Importing your backend logic directly!

# 1. Page Configuration
st.set_page_config(
    page_title="My RAG Tutor",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Personal RAG Assistant")
st.write("Ask questions about your uploaded documents.")

# 2. Session State
# This keeps track of the chat history so it doesn't disappear when you click buttons.
if "messages" not in st.session_state:
    st.session_state.messages = []

# 3. Display Chat History
# We loop through the saved messages and display them on the screen.
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 4. Handle User Input
# This creates the chat box at the bottom.
if prompt := st.chat_input("What would you like to know?"):
    
    # A. Display the user's message immediately
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Save user message to history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # B. Generate the response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            # Call your existing function from rag.py
            result = ask_rag(prompt)
            
            answer = result["answer"]
            sources = result["sources"]
            
            # Display the answer
            st.markdown(answer)
            
            # Display sources in a collapsible box
            if sources:
                with st.expander("📚 View Sources"):
                    for source in sources:
                        st.write(f"- {source}")
    
    # Save assistant message to history
    st.session_state.messages.append({"role": "assistant", "content": answer})