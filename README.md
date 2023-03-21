# Graph databases - Introduction

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the packages you need.

```bash
pip install -r requirements.txt
```

## Creating a graph database using a CSV file

```python
import pandas as pd
from neo4j import GraphDatabase

driver=GraphDatabase.driver(uri="bolt://localhost:7687",auth=("neo4j","password"))
session=driver.session()

df=pd.read_csv("stations.csv")

trains=df["LINE"].unique()

q1="""
MERGE(A:TRAIN{NAME:$train_name})
MERGE(B:STATION{NAME:$station_name})
MERGE (A)-[:GOES_TO]->(B)
"""
for tname in trains:
    x=df.groupby("LINE")[["NAME","LINE"]].get_group(tname)["NAME"]
    for sname in x:
        p={"train_name":tname,"station_name":sname}
        session.run(q1,p)

## License

[MIT](https://choosealicense.com/licenses/mit/)
