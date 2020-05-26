from pydruid.client import *
import pandas as pd

query = PyDruid('http://localhost:8088', 'druid/v2')


ts = query.select(
    datasource='lena-test',
    granularity='second',
    intervals = '2020-05-25/pt9h',
    paging_spec={'pagingIdentifies': {}, 'threshold': 1},
    context={"timeout": 1000}
)
print(ts)
df = ts.export_pandas()
print(df.head())