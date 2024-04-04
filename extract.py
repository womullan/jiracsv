""" basic script to call jiraone extrsact"""
from jiraone import issue_export, LOGIN
import argparse


description = __doc__
formatter = argparse.RawDescriptionHelpFormatter
parser = argparse.ArgumentParser(description=description,
                                     formatter_class=formatter)

parser.add_argument('-u', '--uname', default='rubinjiraapiaccess@gmail.com', help="""Username for Jira .""")
parser.add_argument('-p', '--passwd', help="""Jira Password for user.""")

args = parser.parse_args()

pw = args.passwd
if pw == 'TOKEN':
   with open('TOKEN', 'r') as file:
    pw = file.read().strip()

username = args.uname

config = {"user": f"{username}",
        "password": f"{pw}",
        "url": "https://rubinobs.atlassian.net"}

LOGIN(**config)

query = "filter=11498"
outfile="jira.csv"

issue_export(jql=query, final_file=outfile)


