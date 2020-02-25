# OSD
for querying a domainname's IP address and its location

input : a json from the dataset

output : a json as ```{
	"www.baidu.com" : {
		"subDomain" : {
			"baidu.com" : [{ ip: '75.126.215.88',
				country: '美国',
				area: '',
				region: '德克萨斯',
				city: '达拉斯',
				county: 'XX',
				isp: 'XX',
				country_id: 'US',
				area_id: '',
				region_id: 'US_143',
				city_id: 'US_1099',
				county_id: 'xx',
				isp_id: 'xx' 
			}, {.....}],
			"www.baidu.com" : [{ ip: '75.126.215.88',
				country: '美国',
				area: '',
				region: '德克萨斯',
				city: '达拉斯',
				county: 'XX',
				isp: 'XX',
				country_id: 'US',
				area_id: '',
				region_id: 'US_143',
				city_id: 'US_1099',
				county_id: 'xx',
				isp_id: 'xx' 
			}, {......}]
		}
	}```
