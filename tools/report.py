from langchain.tools import StructuredTool
from pydantic.v1 import BaseModel


def write_report(filename, html):
  with open(filename, 'w') as f:
    f.write(html)


class WriteReportArgsSchema(BaseModel):
  filename: str
  html: str


write_report_tool = StructuredTool.from_function(
    args_schema=WriteReportArgsSchema,
    name='write_report',
    description='Write an html file to the disk. Use this tool whenever someoone asks for a report',
    func=write_report
)
