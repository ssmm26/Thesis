__author__ = 'minasoltangheis'
# ----------------------------------
# To get the files in articles directory and clean  the HTMl part and save the resulting text in
# result directory
# ----we do these lines-------------start:
# import os
# import nltk
# import codecs
# src_dir = '/Users/minasoltangheis/PycharmProjects/ProcessHTMLToUTF8FilesOnly/articles'
# # target for saving in results directory
# target_dir = "/Users/minasoltangheis/PycharmProjects/ProcessHTMLToUTF8FilesOnly/results"
#
# all_text=''
# i=0
# def removeNonAscii(s):
#     return "".join(filter(lambda x: ord(x)<128, s))
#
# for file in os.listdir(src_dir):
#     file_name = os.path.join(src_dir, file)
#     out_file = os.path.join(target_dir, str(i)+'.txt')
#     # if file.endswith(".html"):
#         # print file
#     with open(file_name, "r+") as fi, open(out_file, "w") as fo:
#         all_text= nltk.clean_html(fi.read())
#         fo.write(all_text)
#         i+=1
# # -----------------End of code for reading from articles and deleting HTML and saving the result in the results directory
#
#



# To get the text files that have the whole JSON file in results directory and
# clean the Non ASCII characters and &mp; character and
# then select only 'description' field of the JSON and store it in DescriptionOnly Directory
#
# --Cleaning NON ASCII and only selection Description------------------ start
# import os
# import nltk
# import json
# import re
# src_dir = '/Users/minasoltangheis/PycharmProjects/ProcessHTMLToUTF8FilesOnly/results'
# # target for saving in DescriptionOnly directory
# target_dir = "/Users/minasoltangheis/PycharmProjects/ProcessHTMLToUTF8FilesOnly/DescriptionOnly"
# all_text=''
# i=0
# def removeNonAscii(s):
#     return "".join(filter(lambda x: ord(x)<128, s))
# def removeNonAscii1(s):
#      return (filter(lambda x: ord(x)<128, s))
# def removeNonAscii2(s):
#      return re.sub(ur'\\u[0-9a-zA-z]+','',s)
# for file in os.listdir(src_dir):
#     file_name = os.path.join(src_dir, file)
#     out_file = os.path.join(target_dir, str(i)+'.txt')
#     # if file.endswith(".html"):
#         # print file
#     with open(file_name, "r+") as fi, open(out_file, "w") as fo:
#         try:
#             all_text=json.loads(fi.read())["description"]
#             all_text = removeNonAscii2(all_text)
#             # all_text=   (re.sub(ur'\\u[0-9a-zA-z]+','',fileToread.read()))
#             #      print all_text
#             all_text= re.sub(ur'&amp;','',all_text,re.UNICODE)
#             # print all_text
#             fo.write(all_text)
#             print fi ,"  ", i
#             i+=1
#         except:
#             pass
# -------------------------------------------Description only--------End----------------------------------

#
## To get the text files that have the whole JSON file in results directory and
# clean the Non ASCII characters and &mp; and &gt; character and
# then select only 'description' field of the JSON and store it in SkillsAndExperience Directory

# --Cleaning NON ASCII and only selection SkillsAndExperience------------------ start
# import os
# import nltk
# import json
# import re
# src_dir = '/Users/minasoltangheis/PycharmProjects/ProcessHTMLToUTF8FilesOnly/results'
# # target for saving in DescriptionOnly directory
# target_dir = "/Users/minasoltangheis/PycharmProjects/ProcessHTMLToUTF8FilesOnly/SkillsAndExperience"
# all_text=''
# i=0
# def removeNonAscii(s):
#     return "".join(filter(lambda x: ord(x)<128, s))
# def removeNonAscii1(s):
#      return (filter(lambda x: ord(x)<128, s))
# def removeNonAscii2(s):
#      return re.sub(ur'\\u[0-9a-zA-z+]+','',s)
# for file in os.listdir(src_dir):
#     file_name = os.path.join(src_dir, file)
#     out_file = os.path.join(target_dir, str(i)+'.txt')
#     # if file.endswith(".html"):
#         # print file
#     with open(file_name, "r+") as fi, open(out_file, "w") as fo:
#         try:
#             all_text=json.loads(fi.read())["skillsAndExperience"]
#             all_text = removeNonAscii2(all_text)
#             # all_text=   (re.sub(ur'\\u[0-9a-zA-z]+','',fileToread.read()))
#             #      print all_text
#             all_text= re.sub(ur'&amp;','',all_text,re.UNICODE)
#             all_text=re.sub(ur'&gt;','',all_text,re.UNICODE)
#             # print all_text
#             fo.write(all_text)
#             print fi ,"  ", i
#             i+=1
#         except:
#             pass
# Previous way of doing it
# ---------------The New way of getting SkillsAndExperience section
import os
import nltk
import json
import re
src_dir = '/Users/minasoltangheis/PycharmProjects/ProcessHTMLToUTF8FilesOnly/results'
# target for saving in DescriptionOnly directory
target_dir = "/Users/minasoltangheis/PycharmProjects/ProcessHTMLToUTF8FilesOnly/SkillsAndExperience"
all_text=''
i=0
def removeNonAscii(s):
    return "".join(filter(lambda x: ord(x)<128, s))
def removeNonAscii2(s):
     return re.sub(ur'\\u[0-9a-zA-z+]+','',s)
for file in os.listdir(src_dir):
    file_name = os.path.join(src_dir, file)
    out_file = os.path.join(target_dir, str(i)+'.txt')

    with open(file_name, "r+") as fi:
        myString = fi.read()
        myString = removeNonAscii2(myString)
        sources = json.loads(myString)
        if sources.has_key('skillsAndExperience') and sources.has_key('description'):
            all_text = sources["skillsAndExperience"]
            all_text += '\n'
            all_text += sources["description"]

            print i, all_text
            with open(out_file, "w") as fo:

                fo.write(all_text)
                i+=1


#
# -------------------------------------------SkillsAndExperience only--------End----------------------------------

#
#

## To get the text files that have the whole JSON file in results directory and
# clean the Non ASCII characters and &mp; and &gt; character and
# then select  'description' and  'skillsAndExperience' fields of a  JSON file
# and store it in SkillsAndExperience Directory

# --Cleaning NON ASCII and  selection description and SkillsAndExperience------------------ start
# import os
# import nltk
# import json
# import re
# src_dir = '/Users/minasoltangheis/PycharmProjects/ProcessHTMLToUTF8FilesOnly/results'
# # target for saving in DescriptionAndSkillsANdExperienceTogether directory
# target_dir = "/Users/minasoltangheis/PycharmProjects/ProcessHTMLToUTF8FilesOnly/DescriptionAndSkillsANdExperienceTogether"
# all_text=''
# i=0
# def removeNonAscii(s):
#     return "".join(filter(lambda x: ord(x)<128, s))
# def removeNonAscii1(s):
#      return (filter(lambda x: ord(x)<128, s))
# def removeNonAscii2(s):
#      return re.sub(ur'\\u[0-9a-zA-z+]+','',s)
# for file in os.listdir(src_dir):
#     file_name = os.path.join(src_dir, file)
#     out_file = os.path.join(target_dir, str(i)+'.txt')
#
#     with open(file_name, "r+") as fi:
#         myString = fi.read()
#         myString = removeNonAscii2(myString)
#         sources = json.loads(myString)
#         if sources.has_key('skillsAndExperience') and sources.has_key('description'):
#             all_text = sources["skillsAndExperience"]
#             all_text += '\n'
#             all_text += sources["description"]
#
#             print i, all_text
#             with open(out_file, "w") as fo:
#
#                 fo.write(all_text)
#                 i+=1
#
#


# ---------------------description and SkillsAndExperience only--------End----------------------------------
