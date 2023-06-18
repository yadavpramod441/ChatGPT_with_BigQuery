### Importing Libraries
from google.cloud import bigquery
import streamlit as st
from sqlalchemy  import *
from sqlalchemy.engine import create_engine
from sqlalchemy.schema import *
import os
from langchain.agents  import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit 
from langchain.sql_database import SQLDatabase 
from langchain.llms.openai import OpenAI 
from langchain.agents import AgentExecutor 


##### Code

service_account_file = "/work/avian-light-210704-1eadc5b5acc1.json" ### Service Account Key Path

# Change to where your service account key file is located
project  = "avian-light-210704"
dataset = "Pramod_Attribution"
table = "ROR"
sqlalchemy_url  = f'bigquery://{project}/{dataset}?credentials_path={service_account_file}'

os.environ["OPENAI_API_KEY"]="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" ### Open API Key

db = SQLDatabase.from_uri(sqlalchemy_url)
#llm =OpenAI(temperature=0,model="text-embedding-ada-002	")
llm =OpenAI(temperature=0,model="text-davinci-003") ### Type of embedding
toolkit =SQLDatabaseToolkit(db=db,llm=llm)
agent_executor =create_sql_agent(llm=llm,toolkit=toolkit,verbose=False,top_k=1000)

st.title("Querying RoR Dataset")

# agent_executor.run("""In ROR Dataset, can you check how many insititutions are active in Australia 
# after 2010. Can you also let me know how many number of institition in each type?
# """)
