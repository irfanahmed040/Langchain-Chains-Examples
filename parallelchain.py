from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()

model = ChatOpenAI()

prompt1 = PromptTemplate(
    template="Generate short and simple notes from the following text\n {text}",
    input_variables=['text']
)

prompt2 = PromptTemplate(
    template="Generate 5 short questions & answers from the following text \n {text}",
    input_variables=['text']
)

prompt3 = PromptTemplate(
    template="Merge the provided notes and quiz into a single document\nnotes -> {notes} and quiz -> {quiz}",
    input_variables=['notes', 'quiz']
)

parser = StrOutputParser()

parallel_chain  = RunnableParallel({
    'notes':prompt1 | model | parser,
    'quiz':prompt2 | model | parser
})

merge_chain = prompt3 | model | parser

chain = parallel_chain|merge_chain
text = """Scikit-learn is one of the most widely used machine learning libraries in Python. It is designed to provide simple and efficient tools for data analysis, data mining, and machine learning, making it especially popular among beginners as well as experienced developers. The library is built on top of other fundamental Python libraries such as NumPy, SciPy, and Matplotlib, which provide support for numerical computation, scientific operations, and visualization. Because of this strong foundation, Scikit-learn is both powerful and easy to use.

One of the main advantages of Scikit-learn is its consistent and user-friendly API. Most machine learning models in the library follow the same pattern: create a model, train it using the fit() method, make predictions using predict(), and evaluate performance using built-in metrics. This uniform structure makes it easy to switch between different algorithms without changing much code. Scikit-learn includes a large collection of algorithms for classification, regression, clustering, dimensionality reduction, and model selection.

For classification tasks, Scikit-learn provides algorithms such as Logistic Regression, Decision Trees, Random Forests, Support Vector Machines, and k-Nearest Neighbors. For regression problems, it includes Linear Regression, Ridge Regression, Lasso, and many others. The library also offers clustering techniques like K-Means and DBSCAN, which are useful when working with unlabeled data. In addition, Scikit-learn provides preprocessing tools for scaling, normalization, encoding categorical variables, and handling missing values, which are essential steps in any machine learning pipeline.

Another important feature of Scikit-learn is its support for model evaluation and tuning. It provides tools like cross-validation, grid search, and performance metrics that help in selecting the best model for a given dataset. Because of its simplicity, flexibility, and strong community support, Scikit-learn is often the first choice for machine learning projects in Python."""

result = chain.invoke({'text':text})

print(result)

chain.get_graph().print_ascii()
