import urllib2

def get_product_url(list):
    url_list = []
    base_url = "https://www.amazon.com/dp/"
    for i in range(len(list)):
        url_list.append(base_url + list[i])
    return url_list

def get_asin_code_list(source, sub):
    asin_list = []
    index = 0

    for c in source:
        if c == sub[0]:
            if source[index:index+len(sub)] == sub:
                asin_list.append(get_asin_code(source,index+11))
                #print get_asin_code(source,index+11)
        index += 1
    return asin_list

def get_asin_code(source,index):
    asin_code = ""
    while True:
        if page_source[index] != '\"':
            asin_code += source[index]
            index += 1
        else:
            break
    return asin_code


url_link = raw_input("URL: ")
opener = urllib2.build_opener()
opener.addheaders = [('User-Agent','Mozilla/5.0')]
page_source = opener.open(url_link).read()
f = open("source.txt","w+")
f.write(page_source)

asin = "data-asin=\""

#print page_source
#ind_str(page_source,"data-asin=\"")
#index = find_str(page_source,"data-asin=\"") + 11

print get_product_url(get_asin_code_list(page_source,asin))
