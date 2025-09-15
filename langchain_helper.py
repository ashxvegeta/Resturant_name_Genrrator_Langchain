from secretkey import gemini_api_key
import os
os.environ["GOOGLE_API_KEY"] = gemini_api_key
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.chains import SequentialChain
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.6)
def recommend_restaurants_name_with_items(cuisine):
    # chain 1 restaurant name
    PromptTemplate_name = PromptTemplate(
        input_variables=["cuisine"],
        template="Give me only ONE short name for a {cuisine} restaurant, nothing else."
    )
    name_chain = LLMChain(llm=llm, prompt=PromptTemplate_name, output_key="restaurant_name")

    # chain 2 menu items
    prompt_template_items = PromptTemplate(
        input_variables=["restaurant_name"],
        template="Give me a list of three {restaurant_name} that are used in Indian cooking. Respond in comma separated format, without any explanation."
    )
    food_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key="menu_items")


    sequential_chain = SequentialChain(
        chains=[name_chain, food_chain],
        input_variables=["cuisine"],
        output_variables=["restaurant_name","menu_items"]
    )

    response = sequential_chain({"cuisine": cuisine})

    return response

if __name__ == "__main__":
    print(recommend_restaurants_name_with_items("Indian"))

