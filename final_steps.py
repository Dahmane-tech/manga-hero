import requests
import natsort
import re
import json
import base64



def clean_string(s):
    # Remove non-Latin, non-Arabic, non-numeric, and non-punctuation characters
    s = re.sub(r'[^\w\s\d!"#\$%&\\\'\(\)\*\+,\-\.\/:;<=>\?@\[\]\^_`\{\|\}\~]', '', s)
    # Remove Chinese, Hebrew, Japanese, and Korean characters
    s = re.sub(r'[\u0590-\u05FF\u4E00-\u9FFF\u3040-\u309F\u30A0-\u30FF\u3130-\u318F\uAC00-\uD7AF]', '', s)
    # Replace spaces with underscores<
   
    return s
 # Define the access token and repository information
access_token = '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'
repo_owner = 'Dahmane-tech'
repo_name = 'scrap-manga'   


# Read the input data from file

data = json.load(open('output.json', 'r'))

manga_index = None
for i, item in enumerate(data):
    if 'title' in item and 'description' in item and 'image_url' in item and 'chapters' in item:
        manga_index = i
        break

if manga_index is None:
    print("Error: Manga info not found in input data.")
    exit()

# Move the dictionary with the manga info to the beginning of the list
manga_info = data.pop(manga_index)
data.insert(0, manga_info)
    
data[0]['chapters'] = [c for c in data[0]['chapters'] if c is not None]
title = data[0]['title']

# Loop over all elements starting from the second one
for element in data[1:]:
    # Add the element to the "chapters" key of the first element
    data[0]["chapters"].append(element)

# Remove all elements except the first one
data = [data[0]]
sorted_chapters = natsort.natsorted(data[0]['chapters'], key=lambda x: x['chapter_title'])
data[0]['chapters'] = sorted_chapters

# Clean the strings in the JSON
data[0]["title"] = clean_string(title)
# Define the URL to create a new file in the repository
url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{data[0]["title"]}.json'
print(data[0]["title"])
data[0]["description"] = clean_string(data[0]["description"])
for i in range(len(data[0]["chapters"])):
    current_chapter_title = data[0]["chapters"][i]['chapter_title']
    data[0]["chapters"][i]['chapter_title'] = clean_string(current_chapter_title)

# Write the cleaned data to file
with open('output.json', 'w') as f:
    json.dump(data, f)
file_content_encoded = base64.b64encode(json.dumps(data).encode('utf-8')).decode('utf-8')


# Define the request headers
headers = {
    'Authorization': f'token {access_token}',
    'Content-Type': 'application/json'
}# Define the request data
adata = {
    'message': 'Add backup.json file',
    'content': file_content_encoded
}
# Send the request to create the new file
response = requests.put(url, headers=headers, data=json.dumps(adata))

# Print the response
if response.ok:
    print('The file was successfully added to the repository.')
else:
    print('Error:', response.json()['message'])