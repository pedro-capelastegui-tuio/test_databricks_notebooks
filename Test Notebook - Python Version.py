# Databricks notebook source
# MAGIC %md
# MAGIC ## Test databricks environments for version controlled notebooks
# MAGIC Testing file update

# COMMAND ----------

from platform import python_version
print(python_version())
assert python_version() >= "3.12.3", "Wrong python version - please check databricks notebook environment version. >=v3 recommended."



