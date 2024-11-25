"""
Author: MK Khodadadi
Latest Modification Date: November 25, 2024
"""

prompt_template = """
According to provided information in json format as your source data related to a few places in Munich, please answer the question straight without providing any additional information.

Source data section will start with <source_data> and ends with </source_data>
Format instructions section will start with <format_instructions> and ends with </format_instructions>
Question section will start with <question> and ends with </question>

<source data>
{source_data}
</source data>

<format_instructions>
{format_instructions}
</format_instructions>

<question>
{question}
</question>

answer: 
"""