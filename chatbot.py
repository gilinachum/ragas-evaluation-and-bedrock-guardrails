import streamlit as st
from llm import ask

# Streamlit app
def main():
    st.title("BedrockCars Chatbot")
    
    # Get user input
    question = st.text_input("Ask a question:")
    
    # If the user enters a question and clicks the button
    if st.button("Submit"):
        # Generate the response
        response = ask(question)
        
        # Display the response
        st.success(response)

if __name__ == "__main__":
    main()
    #print(generate_response("how are you?"))
