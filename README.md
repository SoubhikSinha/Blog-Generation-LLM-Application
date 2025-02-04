# Blog Generation - Llama 2

## Acknowledgement
[](https://github.com/SoubhikSinha/LLM-LangChain-PineCone-VectorDB#acknowledgement)

I would like to extend my sincere thanks to  [Krish Naik](https://github.com/krishnaik06)  for his invaluable content and guidance, which helped me build this project. This project wouldn't have been possible without his educational resource(s).

<br>


## About the Project
This project provides hands-on experience with Meta's [Llama-2](https://www.llama.com/llama2/) model. The goal is to develop a **Streamlit application for blog generation**, allowing users to effortlessly generate blog content.

### Features:
-   Users can input a **blog topic**, specify the **word count**, and define the **target audience**.
-   The application then generates a well-structured blog based on the given inputs.

Since the full **Llama-2** model is massive, we use a [compressed version of Llama-2](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/blob/main/llama-2-7b-chat.ggmlv3.q8_0.bin) for simplicity and efficiency.

<br>

## How to Run the Project ?
### **1. Clone the Repository**
Clone the repository to your local machine :
```bash
git clone https://github.com/SoubhikSinha/Blog-Generation-LLM-Application.git
```

<br>

### **2. Create a Virtual Environment**
Navigate to the repository's root directory and create a Conda virtual environment :
```bash
conda create --prefix ./venv python=3.11 -y
```

<br>

### **3. Activate the Conda Environment**
Activate the newly created environment :
```bash
conda activate venv/
```

<br>

### **4. Install Required Libraries**
Install all the necessary dependencies :
```bash
pip install -r requirements.txt
```

<br>


### **5. Download the Llama-2 Model from Hugging Face**
1.  Download the Llama-2 model from Hugging Face:  
    **[Download Link](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/blob/main/llama-2-7b-chat.ggmlv3.q8_0.bin)**
2.  Store the downloaded model in the following directory format :
	```bash
	root/models/llama-2-7b-chat.ggmlv3.q8_0.bin
	```

<br>    

### **6. Run the Streamlit Application**
To start the Streamlit application, run the following command in your CLI (Command Line Interface) or Terminal :
```bash
streamlit run app.py
```

<br>

### **7. Test the Application**

Once the application is running, enter the required details (blog topic, word count, and target audience) to generate blog content.

<br>

### **8. Stop the Server**

To shut down the application, press the following command:
```bash
CTRL + C
```
