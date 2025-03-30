from bs4 import BeautifulSoup


data_ids = []
# Open the file and read its contents
for i in range(1, 27):
    with open(f"/Users/jd/Documents/PremierLeagueModel/PremierLeagueModel/htmlscripts/Bundesliga/round{i}.txt", "r", encoding="utf-8") as file:
        content = file.read()
        soup = BeautifulSoup(content, "html.parser")
        for element in soup.find_all(attrs={"data-id": True}):
            data_ids.append(element["data-id"])



# Print the array of data-id values
print(data_ids)
