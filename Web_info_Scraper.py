import requests
import os
from bs4 import BeautifulSoup

#subject to change for the web data source url
url = "https://www.tripadvisor.com/Restaurant_Review-g31377-d334357-Reviews-Four_Peaks_Restaurant-Tempe_Arizona.html"
url_page2 = "https://www.tripadvisor.com/Restaurant_Review-g31377-d334357-Reviews-or10-Four_Peaks_Restaurant-Tempe_Arizona.html#REVIEWS"

r = requests.get(url)
r2 = requests.get(url_page2)

soup = BeautifulSoup(r.content,"html.parser")
#soup = BeautifulSoup(r2.content)

#print(soup.prettify())

#links = soup.find_all("a")

#For finding all review content titles:
review_content_title = soup.find_all("span",{"class":"noQuotes"})

#For finding all review contents:
review_content = soup.find_all("div",{"class":"entry"})

#For finding review stars
review_star = soup.find_all("img",{"class":"sprite-rating_s_fill"})

#For finding review times
review_time = soup.find_all("span",{"class":"ratingDate"})

#For finding user name
user_names = soup.find_all("div",{"class","username"})

#For finding user levels
user_levels = soup.find_all("div",{"class","levelBadge"})

#For finding user reviews
user_review_num = soup.find_all("span",{"class","badgeText"})

#For finding user member time
user_mem_time = soup.find_all("ul",{"class","memberdescription"})

#Making things easier to read



#File Stream for review times 
#dir_path = os.path.join(self.feed, self.address)
script_dir = os.path.dirname(os.path.abspath(__file__))
dest_dir = os.path.join(script_dir, 'data1')
try:
    os.makedirs(dest_dir)
except OSError:
    pass # already exists

f = open('data1/review_time.txt','w')

for item in review_time:#user_mem_time:#user_review_num:#user_levels:#user_names:#review_time:#review_star:#review_content:#review_content_title:
	f.write(item.get("title")+"\t")   #print(item.content[1].text)#print(item.text)#item.get("class")#print(item.text)#item.get("title")    #item.get("alt") #print(item.text,";")  #semi colon for Excel separation(later use)
	f.write(item.text)
	



f.close()
print "data has been correctly written into review_time.txt"#print(item.text)


# File Stream for Content Titles
f = open('data1/content_titles.txt','w')

for item in review_content_title:#user_mem_time:#user_review_num:#user_levels:#user_names:#review_time:#review_star:#review_content:#review_content_title:
    #print(item.content[1].text)#print(item.text)#item.get("class")#print(item.text)#item.get("title")    #itemitem.text,";")  #semi colon for Excel separation(later use)
	f.write(item.text+";\n")

print "data has been correctly written into content_titles.txt"#print(item.text)

f.close()


# File Stream for Review Content
f = open('data1/review_content.txt','w')

for item in review_content:#user_mem_time:#user_review_num:#user_levels:#user_names:#review_time:#review_star:#review_content:#review_content_title:
	f.write(item.text.encode('ascii','ignore'))
	
print "data has been correctly written into review_contents.txt"#print(item.text)

f.close()



# File Stream for Review Stars
f = open('data1/review_stars.txt','w')

for item in review_star:#user_mem_time:#user_review_num:#user_levels:#user_names:#review_time:#review_star:#review_content:#review_content_title:
	f.write(item.get("alt")+"\n")

print "data has been correctly written into review_stars.txt"#print(item.text)

f.close()

# File Stream for User Names
f = open('data1/user_names.txt','w')

for item in user_names:#user_mem_time:#user_review_num:#user_levels:#user_names:#review_time:#review_star:#review_content:#review_content_title:
	f.write(item.text+"\n")

print "data has been correctly written into user_names.txt"#print(item.text)

f.close()

# File Stream for User Levels
f = open('data1/user_levels.txt','w')

for item in user_levels:#user_mem_time:#user_review_num:#user_levels:#user_names:#review_time:#review_star:#review_content:#review_content_title:
	f.write(str(item.get("class"))+"\n")

print "data has been correctly written into user_levels.txt"#print(item.text)

f.close()


# File Stream for User Review Number
f = open('data1/user_review_num.txt','w')

for item in user_review_num:#user_mem_time:#user_review_num:#user_levels:#user_names:#review_time:#review_star:#review_content:#review_content_title:
	f.write(item.text+"\n")

print "data has been correctly written into user_review_num.txt"#print(item.text)

f.close()



#**********************************FOR PAGE 2 CONTENT**********************************************


soup2 = BeautifulSoup(r2.content,"html.parser")

#For finding all review content titles:
review_content_title2 = soup2.find_all("span",{"class":"noQuotes"})

#For finding all review contents:
review_content2 = soup2.find_all("div",{"class":"entry"})

#For finding review stars
review_star2 = soup2.find_all("img",{"class":"sprite-rating_s_fill"})

#For finding review times
review_time2 = soup2.find_all("span",{"class":"ratingDate"})

#For finding user name
user_names2 = soup2.find_all("div",{"class","username"})

#For finding user levels
user_levels2 = soup2.find_all("div",{"class","levelBadge"})

#For finding user reviews
user_review_num2 = soup2.find_all("span",{"class","badgeText"})




script_dir = os.path.dirname(os.path.abspath(__file__))
dest_dir = os.path.join(script_dir, 'data2')
try:
    os.makedirs(dest_dir)
except OSError:
    pass # already exists

f = open('data2/review_time.txt','w')

for item in review_time:#user_mem_time:#user_review_num:#user_levels:#user_names:#review_time:#review_star:#review_content:#review_content_title:
	f.write(item.get("title")+"\t")   #print(item.content[1].text)#print(item.text)#item.get("class")#print(item.text)#item.get("title")    #item.get("alt") #print(item.text,";")  #semi colon for Excel separation(later use)
	f.write(item.text)
	



f.close()
print "data has been correctly written into review_time.txt"#print(item.text)


# File Stream for Content Titles
f = open('data2/content_titles.txt','w')

for item in review_content_title2:#user_mem_time:#user_review_num:#user_levels:#user_names:#review_time:#review_star:#review_content:#review_content_title:
    #print(item.content[1].text)#print(item.text)#item.get("class")#print(item.text)#item.get("title")    #itemitem.text,";")  #semi colon for Excel separation(later use)
	f.write(item.text+";\n")

print "data has been correctly written into content_titles.txt"#print(item.text)

f.close()


# File Stream for Review Content
f = open('data2/review_content.txt','w')

for item in review_content2:#user_mem_time:#user_review_num:#user_levels:#user_names:#review_time:#review_star:#review_content:#review_content_title:
	f.write(item.text.encode('ascii','ignore'))
	
print "data has been correctly written into review_contents.txt"#print(item.text)

f.close()



# File Stream for Review Stars
f = open('data2/review_stars.txt','w')

for item in review_star2:#user_mem_time:#user_review_num:#user_levels:#user_names:#review_time:#review_star:#review_content:#review_content_title:
	f.write(item.get("alt")+"\n")

print "data has been correctly written into review_stars.txt"#print(item.text)

f.close()

# File Stream for User Names
f = open('data2/user_names.txt','w')

for item in user_names2:#user_mem_time:#user_review_num:#user_levels:#user_names:#review_time:#review_star:#review_content:#review_content_title:
	f.write(item.text+"\n")

print "data has been correctly written into user_names.txt"#print(item.text)

f.close()

# File Stream for User Levels
f = open('data2/user_levels.txt','w')

for item in user_levels2:#user_mem_time:#user_review_num:#user_levels:#user_names:#review_time:#review_star:#review_content:#review_content_title:
	f.write(str(item.get("class"))+"\n")

print "data has been correctly written into user_levels.txt"#print(item.text)

f.close()


# File Stream for User Review Number
f = open('data2/user_review_num.txt','w')

for item in user_review_num2:#user_mem_time:#user_review_num:#user_levels:#user_names:#review_time:#review_star:#review_content:#review_content_title:
	f.write(item.text+"\n")

print "data has been correctly written into user_review_num.txt"#print(item.text)

f.close()