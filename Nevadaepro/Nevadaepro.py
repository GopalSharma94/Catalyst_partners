from scrapy import Selector
import re
import requests
import json

data_path = 'C:\\Users\\ASUS\\Downloads\\Catalyst_partners\\Nevadaepro\\'
download_path = 'C:\\Users\\ASUS\\Downloads\\Catalyst_partners\\Nevadaepro\\Doc\\'
url = 'https://nevadaepro.com/bso/view/search/external/advancedSearchBid.xhtml?openBids=true'

#################### Page & Bid ID ##############################

data_list = []
for page in range(0,50,25):
    print(page)
    headers = {
        'Accept': 'application/xml, text/xml, */*; q=0.01',
        'Accept-Language': 'en-US,en;q=0.9,hi;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': 'XSRF-TOKEN=1391f6c2-8708-4ba6-8eff-997865bf17e3; JSESSIONID=1A092E4669F050A5BDFE7F24FB9F12A9; dtCookie=v_4_srv_13_sn_95EA3A2046C306C635777D627127034B_perc_100000_ol_0_mul_1_app-3A37bc123ce5d9a8ed_0; _ga=GA1.1.1558658757.1707984029; AWSALB=eCaLbrnjJve7vinbiwmJg9NSmqLj9oQ6VlgjrsyolU8IlrrSNKMiq+EtjU8hQtvaq3hRcew9XvoWmClhm3HUZfU1iagJW8yPyFtmW27GPQEv4LLH3QBN2btfzBSK; AWSALBCORS=eCaLbrnjJve7vinbiwmJg9NSmqLj9oQ6VlgjrsyolU8IlrrSNKMiq+EtjU8hQtvaq3hRcew9XvoWmClhm3HUZfU1iagJW8yPyFtmW27GPQEv4LLH3QBN2btfzBSK; _ga_JGSX0KVE09=GS1.1.1707993180.3.1.1707994427.0.0.0',
        'Faces-Request': 'partial/ajax',
        'Origin': 'https://nevadaepro.com',
        'Referer': 'https://nevadaepro.com/bso/view/search/external/advancedSearchBid.xhtml?openBids=true',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'x-dtpc': '13$394333270_307h7vCHGMIAAQPNFFDGFQFHSRLCNOUKFHBTSC-0e0',
    }
    session_1 = requests.Session()
    resp_cookie = session_1.get(url,verify=False)
    cookies_1 = requests.get(url,verify=False,headers=headers).cookies.get_dict()


    cookies = {
        'XSRF-TOKEN': cookies_1['XSRF-TOKEN'],
        'JSESSIONID': cookies_1['JSESSIONID']

    }




    data = {
        'javax.faces.partial.ajax': 'true',
        'javax.faces.source': 'bidSearchResultsForm:bidResultId',
        'javax.faces.partial.execute': 'bidSearchResultsForm:bidResultId',
        'javax.faces.partial.render': 'bidSearchResultsForm:bidResultId',
        'bidSearchResultsForm:bidResultId': 'bidSearchResultsForm:bidResultId',
        'bidSearchResultsForm:bidResultId_pagination': 'true',
        'bidSearchResultsForm:bidResultId_first': str(page),
        'bidSearchResultsForm:bidResultId_rows': '25',
        'bidSearchResultsForm:bidResultId_encodeFeature': 'true',
        'bidSearchResultsForm': 'bidSearchResultsForm',
        '_csrf': cookies_1['XSRF-TOKEN'],
        'openBids': 'true',
        # 'javax.faces.ViewState': '-6456176669437291930:4569148265894656451',
    }

    resp_1 = requests.post('https://nevadaepro.com/bso/view/search/external/advancedSearchBid.xhtml',cookies=cookies, headers=headers,data=data,verify=False)

    response_1 = Selector(text=resp_1.text)

    Bid_Solicitation_data = response_1.xpath('//tr[@class="ui-widget-content ui-datatable-even"]')

    for bid in Bid_Solicitation_data:
        Bid_Solicitation = bid.xpath('.//a/text()').extract_first()
        print(Bid_Solicitation)
########################## Data part #########################
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'en-US,en;q=0.9,hi;q=0.8',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            # 'Cookie': 'JSESSIONID=621110306F11F69A2B2879C9A4F0AC09; XSRF-TOKEN=1391f6c2-8708-4ba6-8eff-997865bf17e3; dtCookie=v_4_srv_13_sn_95EA3A2046C306C635777D627127034B_perc_100000_ol_0_mul_1_app-3A37bc123ce5d9a8ed_0; _ga=GA1.1.1558658757.1707984029; _ga_JGSX0KVE09=GS1.1.1707984029.1.1.1707984816.0.0.0; AWSALB=1ydo9xYxXzs0coUsIkTXrthIuZmFK65kk0PWvp2Prd0zOLDe4iIV48bjyroJguGBidnd5H00pKjkSg3IMR77kGz2rHjrIdnt4OXOp9+X915qX+yGC8YZMXM3CROG; AWSALBCORS=1ydo9xYxXzs0coUsIkTXrthIuZmFK65kk0PWvp2Prd0zOLDe4iIV48bjyroJguGBidnd5H00pKjkSg3IMR77kGz2rHjrIdnt4OXOp9+X915qX+yGC8YZMXM3CROG',
            'Referer': 'https://nevadaepro.com/bso/view/search/external/advancedSearchBid.xhtml?openBids=true',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        params = {
            'docId': Bid_Solicitation,
            'external': 'true',
            'parentUrl': 'close',
        }

        resp = requests.get('https://nevadaepro.com/bso/external/bidDetail.sdo', params=params,  headers=headers,verify=False)

        response = Selector(text=resp.text)

        data = response.xpath('//td[@align="left"]//table[@role="presentation"]')

        Bid_Number = data[0].xpath('//*[contains(text(), "Bid Number")]//following-sibling::td[1]/text()').extract_first().strip()
        Description = data[0].xpath('//*[contains(text(), "Description")]//following-sibling::td[1]/text()').extract_first().strip()
        Bid_Opening_Date = data[0].xpath('//*[contains(text(), "Bid Opening Date")]//following-sibling::td[1]/text()').extract_first().strip()

        Purchaser = data[1].xpath('//*[contains(text(), "Purchaser")]//following-sibling::td[1]/text()').extract_first().strip()
        Organization = data[1].xpath('//*[contains(text(), "Organization")]//following-sibling::td[1]/text()').extract_first().strip()
        Department = data[2].xpath('//*[contains(text(), "Department")]//following-sibling::td[1]/text()').extract_first().strip()
        Location = data[2].xpath('//*[contains(text(), "Location")]//following-sibling::td[1]/text()').extract_first().strip()
        Fiscal_Year = data[3].xpath('//*[contains(text(), "Fiscal Year")]//following-sibling::td[1]/text()').extract_first().strip()
        Type_Code = data[3].xpath('//*[contains(text(), "Type Code")]//following-sibling::td[1]/text()').extract_first().strip()
        Allow_Electronic_Quote = data[3].xpath('//*[contains(text(), "Allow Electronic Quote")]//following-sibling::td[1]/text()').extract_first().strip()
        Alternate_Id = data[3].xpath('//*[contains(text(), "Alternate Id")]//following-sibling::td[1]/text()').extract_first().strip()
        Required_Date = data[3].xpath('//*[contains(text(), "Required Date")]//following-sibling::td[1]/text()').extract_first().strip()
        Available_Date = data[3].xpath('//*[contains(text(), "Available Date")]//following-sibling::td[1]/text()').extract_first().strip()
        Info_Contact = data[4].xpath('//*[contains(text(), "Info Contact")]//following-sibling::td[1]/text()').extract_first().strip()
        Bid_Type = data[1].xpath('//*[contains(text(), "Bid Type")]//following-sibling::td[1]/text()').extract_first().strip()
        Informal_Bid_Flag = data[1].xpath('//*[contains(text(), "Informal Bid Flag")]//following-sibling::td[1]/text()').extract_first().strip()
        Purchase_Method = data[1].xpath('//*[contains(text(), "Purchase Method")]//following-sibling::td[1]/text()').extract_first().strip()
        Pre_Bid_Conference = data[1].xpath('//*[contains(text(), "Pre Bid Conference")]//following-sibling::td[1]/text()').extract_first().strip()
        Bulletin_Desc = data[1].xpath('//*[contains(text(), "Bulletin Desc")]//following-sibling::td[1]/text()').extract_first().strip()
        Ship_to_Address = ' '.join(map(str,data[1].xpath('//*[contains(text(), "Ship-to Address:")]//following-sibling::td[1]/text()').extract())).strip()
        Bill_to_Address = ' '.join(map(str,data[1].xpath('//*[contains(text(), "Bill-to Address:")]//following-sibling::td[1]//text()').extract())).strip()

        nevadaepro_dict = {'Bid_Number': Bid_Number, 'Description': Description, 'Bid_Opening_Date': Bid_Opening_Date,
                           'Purchaser': Purchaser,"Organization":Organization,"Department":Department,"Location":Location,
                           "Fiscal_Year":Fiscal_Year,"Type_Code":Type_Code,"Allow_Electronic_Quote":Allow_Electronic_Quote,
                           "Alternate_Id":Alternate_Id,"Required_Date":Required_Date,"Available_Date":Available_Date,
                           "Info_Contact":Info_Contact,"Bid_Type":Bid_Type,"Informal_Bid_Flag":Informal_Bid_Flag,"Purchase_Method":Purchase_Method,
                           "Pre_Bid_Conference":Pre_Bid_Conference,"Bulletin_Desc":Bulletin_Desc,"Ship_to_Address":Ship_to_Address,
                           "Bill_to_Address":Bill_to_Address}
        data_list.append({str(Bid_Number):nevadaepro_dict})
    ########################### Download files ######################################
        File_Attachments_list = data[1].xpath('//*[contains(text(), "File Attachments")]//following-sibling::td[1]/a')

        for i in File_Attachments_list:
            download_file_no = re.findall('\d+',i.xpath('.//@href').extract_first())[0]
            file_name = i.xpath('.//text()').extract_first()
            # cookies_2 = {
            #     'JSESSIONID': '621110306F11F69A2B2879C9A4F0AC09',
            #     'XSRF-TOKEN': '1391f6c2-8708-4ba6-8eff-997865bf17e3',
            #     'dtCookie': 'v_4_srv_13_sn_95EA3A2046C306C635777D627127034B_perc_100000_ol_0_mul_1_app-3A37bc123ce5d9a8ed_0',
            #     '_ga': 'GA1.1.1558658757.1707984029',
            #     'AWSALB': '1IYVKcsMYiEvpKkunCQwDWVGWicWvZ6Yua7CcvJki6S/5k1m1DtKRml3EC0lg80tGcIt7GeQaPCu2wqkRbFYuJmF0+6klCnsByFL765QoMFY6Z3/HctTnT/nsz0X',
            #     'AWSALBCORS': '1IYVKcsMYiEvpKkunCQwDWVGWicWvZ6Yua7CcvJki6S/5k1m1DtKRml3EC0lg80tGcIt7GeQaPCu2wqkRbFYuJmF0+6klCnsByFL765QoMFY6Z3/HctTnT/nsz0X',
            #     '_ga_JGSX0KVE09': 'GS1.1.1707988197.2.0.1707988197.0.0.0',
            # }
            headers_2 = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Accept-Language': 'en-US,en;q=0.9,hi;q=0.8',
                'Cache-Control': 'max-age=0',
                'Connection': 'keep-alive',
                'Content-Type': 'application/x-www-form-urlencoded',
                # 'Cookie': 'JSESSIONID=621110306F11F69A2B2879C9A4F0AC09; XSRF-TOKEN=1391f6c2-8708-4ba6-8eff-997865bf17e3; dtCookie=v_4_srv_13_sn_95EA3A2046C306C635777D627127034B_perc_100000_ol_0_mul_1_app-3A37bc123ce5d9a8ed_0; _ga=GA1.1.1558658757.1707984029; AWSALB=1IYVKcsMYiEvpKkunCQwDWVGWicWvZ6Yua7CcvJki6S/5k1m1DtKRml3EC0lg80tGcIt7GeQaPCu2wqkRbFYuJmF0+6klCnsByFL765QoMFY6Z3/HctTnT/nsz0X; AWSALBCORS=1IYVKcsMYiEvpKkunCQwDWVGWicWvZ6Yua7CcvJki6S/5k1m1DtKRml3EC0lg80tGcIt7GeQaPCu2wqkRbFYuJmF0+6klCnsByFL765QoMFY6Z3/HctTnT/nsz0X; _ga_JGSX0KVE09=GS1.1.1707988197.2.0.1707988197.0.0.0',
                'Origin': 'https://nevadaepro.com',
                'Referer': 'https://nevadaepro.com/bso/external/bidDetail.sdo?docId={}&external=true&parentUrl=close'.format(Bid_Number),
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-User': '?1',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
            }

            cookies_2 = requests.get('https://nevadaepro.com/bso/external/bidDetail.sdo?docId={}&external=true&parentUrl=close'.format(Bid_Number),verify=False,headers=headers).cookies.get_dict()

            data_2 = {
                '_csrf': cookies_2['XSRF-TOKEN'],
                'mode': 'download',
                'bidId': Bid_Number,
                'docId': Bid_Number,
                'currentPage': '1',
                'querySql': '',
                'downloadFileNbr': download_file_no,
                'itemNbr': 'undefined',
                'parentUrl': 'close',
                'fromQuote': '',
                'destination': '',
            }

            request_file = requests.post('https://nevadaepro.com/bso/external/bidDetail.sdo', headers=headers_2, cookies=cookies_2, data=data_2,verify=False)
            if '.docx' in file_name:
                with open(download_path+Bid_Number+'_'+download_file_no+'.docx', 'wb') as f:
                    f.write(request_file.content)
            else:
                with open(download_path+Bid_Number+'_'+download_file_no+'.pdf', 'wb') as f:
                    f.write(request_file.content)

with open(data_path +'data.json', 'w') as f:
    json.dump(data_list, f)
print("Hi")