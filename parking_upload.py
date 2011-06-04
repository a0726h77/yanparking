# coding:utf-8

import re
import urllib2


xml_data = """
<list>
<parking><name>玉成國小地下停車場</name><space>84</space><price>電詢</price><datetime>2010-12-28T07:49:10.644920</datetime><geopt>25.0530744,121.5926464</geopt><address>臺北市南港區昆陽街23號</address><total>297</total></parking><parking><name>大安高工地下停車場</name><space>120</space><price>30/1小時</price><detail>(教師優惠月票1000元，限7-19)，全日促銷優惠月票5760元，日間優惠月票4200元(7-20)，夜間優惠月票1500元(20-7) (9-21)計時30元 (21-9)計時10元</detail><datetime>2010-12-28T07:59:19.726622</datetime><geopt>25.032703,121.541038</geopt><address>台北大安區信義路三段166巷6弄12號</address><total>533</total></parking><parking><name>成德立體停車場</name><space>86</space><price>30/1小時</price><detail>促銷優惠月票4800元，里民優惠月票3840元，計時30元，日間優惠月票2400元(7-19)，夜間優惠月票2400元(19-7)</detail><datetime>2010-12-28T08:14:35.462559</datetime><geopt>25.045886,121.586048</geopt><address>台北南港區成福路1號</address><total>180</total></parking><parking><name>威秀影城松壽20</name><space>64</space><price>60元/1小時</price><detail>24小時月票4600元，24小時季票13200元；白天時間月票3500元，白天時間季票9900元</detail><datetime>2011-05-12T08:35:19.124607</datetime><geopt>25.035636,121.567099</geopt><address>台北市信義區松壽路20號</address><total>174</total></parking><parking><name>君悅大飯店地下停車場</name><space>278</space><price>70元/1小時</price><detail>每小時70元，一小時以上每半小時35元</detail><datetime>2011-05-12T08:35:17.947754</datetime><geopt>25.035839,121.563072</geopt><address>台北市信義區松壽路2號</address><total>650</total></parking><parking><name>府前廣場地下停車場</name><space>1041</space><price>30元/1小時</price><detail>123</detail><datetime>2011-05-12T08:35:15.722418</datetime><geopt>25.036536,121.56402</geopt><address>台北市信義區松壽路1號</address><total>2027</total></parking><parking><name>臺北市災害應變中心地下停車場</name><space>23</space><price>30元/1小時</price><detail>地下2層，24小時全自動電腦計時收費；計時30元，全日月票4800元，夜間月票2400元(18-8)，進場車輛限高1.9米。TEL:2337-9616</detail><datetime>2011-05-12T08:35:16.444408</datetime><geopt>25.028661,121.566118</geopt><address>台北市信義區莊敬路391巷11弄2號</address><total>170</total></parking><parking><name>建成國中地下停車場</name><space>51</space><price>30/1小時</price><detail>月票7200元，計時30元，日間月票4800元(8-19)，夜間優惠月票2400元(限19-8)，夜間優惠計時10元(22-8)，自98年12月31日起機車免費</detail><datetime>2010-12-28T08:22:50.898835</datetime><geopt>25.0504161,121.5196442</geopt><address>台北大同區長安西路37號之一</address><total>323</total></parking><parking><name>世貿三館停車場</name><space>--</space><price>40元/1小時</price><datetime>2011-05-12T08:35:17.434981</datetime><geopt>25.035056,121.565389</geopt><address>台北市信義區松壽路6號</address><total>515</total></parking><parking><name>松壽公園地下停車場</name><space>64</space><price>30元/1小時</price><detail>費率詳現場公告</detail><datetime>2011-05-12T08:35:16.175365</datetime><geopt>25.037095,121.56573</geopt><address>台北市信義區松廉路1號</address><total>452</total></parking><parking><name>西松高中地下停車場</name><space>179</space><price>30/1小時</price><detail>計時30元，全日月票5250元，日間優惠月票2800元(7-20)，夜間月票2450元(18-9)，夜間折扣(22-8)計時10元</detail><datetime>2010-12-28T07:47:47.993025</datetime><geopt>25.055812,121.56588</geopt><address>台北松山區健康路325巷19弄1號</address><total>341</total></parking><parking><name>雅祥公園地下停車場</name><space>76</space><price>30元/1小時</price><detail>開場初期6個月優惠促銷，全日月票優惠促銷4800元(原7200元)、里民月票優惠促銷3840元、所在里月票優惠促銷3360元</detail><datetime>2011-05-12T08:35:16.723047</datetime><geopt>25.034786,121.568857</geopt><address>台北市信義區松仁路130號</address><total>204</total></parking><parking><name>立農公園地下停車場</name><space>70</space><price>20元/1小時</price><detail>全日促銷月票3000元(原價4800元，促銷日期自98.10月至99年3月止)</detail><datetime>2011-05-12T08:35:17.007273</datetime><geopt>25.118497,121.503052</geopt><address>台北市北投區承德路七段372號</address><total>205</total></parking><parking><name>辛亥國小地下停車場</name><space>65</space><price>20/1小時</price><detail>全日促銷優惠月票3840元，8-18計時20元，18-8計時10元</detail><datetime>2010-12-28T07:55:05.837265</datetime><geopt>25.00632,121.558556</geopt><address>台北文山區辛亥路四段103號</address><total>131</total></parking><parking><name>萬華國中地下停車場</name><space>242</space><price>20元/1小時</price><detail>夜間優惠計時10元(22-8), 全日促銷優惠月票3000元，日間月票2000元(07:00-19:00)，夜間月票1200元(19:00-08:00)，機車計次20元,機車月票300元</detail><datetime>2011-05-12T08:35:17.691055</datetime><geopt>25.029338,121.499525</geopt><address>台北市萬華區西藏路201號</address><total>508</total></parking><parking><name>威秀影城松壽18</name><space>57</space><price>60元/1小時</price><detail>24小時月票4600元，24小時季票13200元；白天時間月票3500元，白天時間季票9900元</detail><datetime>2011-05-12T08:35:19.393793</datetime><geopt>25.035684,121.56681</geopt><address>台北市信義區松壽路18號</address><total>93</total></parking><parking><name>台北世貿中心展覽大樓地下停車場</name><space>40</space><price>70元/1小時</price><detail>費用僅供參考，若有異動，以現場公告為準</detail><datetime>2011-05-12T08:35:18.320926</datetime><geopt>25.034339,121.560687</geopt><address>台北市信義區基隆路一段333號</address><total>341</total></parking><parking><name>台北世貿中心國貿大樓地下停車場</name><space>109</space><price>70元/1小時</price><detail>一小時以上每半小時35元</detail><datetime>2011-05-12T08:35:18.585853</datetime><geopt>25.03423,121.560591</geopt><address>台北市信義區基隆路一段333號</address><total>185</total></parking><parking><name>附中公園地下停車場</name><space>40</space><price>40元/1小時</price><detail>全日月票5760元，計時40元，(21-8)計時10元</detail><datetime>2011-01-19T16:05:20.942508</datetime><geopt>25.036291,121.542289</geopt><address>台北大安區復興南路一段340巷11號</address><total>125</total></parking><parking><name>台北國際會議中心地下停車場</name><space>60</space><price>70元/1小時</price><detail>一小時以上每半小時35元</detail><datetime>2011-05-12T08:35:18.864323</datetime><geopt>25.034342,121.56091</geopt><address>台北市信義區基隆路一段333號34樓</address><total>394</total></parking><parking><name>興雅國中地下停車場</name><space>189</space><price>20元/1小時</price><detail>月票4800元，日間時段優惠月票2400元(7-19)，夜間月票2400元(限19-8)，(18-8)計時10元</detail><datetime>2011-01-19T16:05:15.998852</datetime><geopt>25.034906,121.572808</geopt><address>台北信義區松德路200巷18號</address><total>447</total></parking><parking><name>峨嵋立體停車場</name><space>420</space><price>40元/1小時 六日50/1小時</price><detail>全日優惠月票4800元，日間月票4000元(10-22)，夜間時段促銷月票500元(21-9)，週一至週五計時40元(10-22)；週六至週日及政府行政機關放假之紀念日及民俗節計時50元(10-22)，其餘時段計時10元(22-10)，機車計次20元(月票300元)</detail><datetime>2011-01-19T16:05:16.280615</datetime><geopt>25.044327,121.505325</geopt><address>台北市萬華區峨嵋街83號</address><total>511</total></parking><parking><name>中山堂地下停車場</name><space>374</space><price>40元/1小時</price><detail>日間月票3600元(7-19)，夜間月票1000元(19-8)，周一至周五(8-20)計時40元，(20-8)計時10元，周六至周日及政府行政機關放假之紀念日及民俗節日(10-20)計時40元，(20-10)計時10元 (本場無所在里里民7折優惠)</detail><datetime>2011-01-19T16:05:16.540859</datetime><geopt>25.043204,121.510036</geopt><address>台北市中正區延平南路98號</address><total>440</total></parking><parking><name>光復北路立體停車場</name><space>關閉</space><price>30元/1小時</price><detail>計時30元，全日月票4800元，全日里民優惠月票3840元，所在里民優惠月票3360元，日間月票2800元(7-19)，98.12.1委外(以公告為最高金額，廠商另有優惠，以現場公告為原則)</detail><datetime>2011-01-19T16:05:16.805563</datetime><geopt>25.048867,121.558351</geopt><address>台北松山區八德路四段17巷9號</address><total>130</total></parking><parking><name>洛陽綜合立體停車場</name><space>901</space><price>20元/1小時</price><detail>小型車： (全日月票原價4800元)，全日月票3300元，日間月票2400元(7-20)，夜間月票900元(20-7)，周一至周五(8-22)計時20元，(22-8)計時10元，周六至周日及政府行政機關放假之紀念日及民俗節日(8-10)計時20元，(10-22)計時30元，(22-8)計時10元2、大型車：計時40元，月票9600元 3、機車：計次20元，月票300元(本場無所在里里民7折優惠)</detail><datetime>2011-01-19T16:05:17.102294</datetime><geopt>25.047595,121.505376</geopt><address>台北市萬華區環河南路一段1號</address><total>1651</total></parking><parking><name>塔城公園地下停車場</name><space>26</space><price>30元/1小時</price><detail>全日優惠月票5760元，夜間月票3000元(21-8)，計時30元 計費單位：停車時數未滿1小時者，以1小時計算收費。停車時數逾1小時以上，其超過之不滿1小時部分，如不逾30分鐘者，以半小時計算；如逾30分鐘者，仍以1小時計算收費。</detail><datetime>2011-01-19T16:05:17.378007</datetime><geopt>25.05064,121.51069</geopt><address>台北市大同區塔城街7號</address><total>162</total></parking><parking><name>百齡高中地下停車場</name><space>188</space><price>40元/1小時 六日50/1小時</price><datetime>2011-01-19T16:05:17.625261</datetime><geopt>25.086151,121.523996</geopt><address>台北市士林區承德路四段175號B1樓</address><total>229</total></parking><parking><name>前港公園地下停車場</name><space>92</space><price>20元/1小時 六日30/1小時</price><detail>(月票4800元)，日間月票3600元(7-19)，週一至週五全日計時20元，週六至週日及政府行政機關放假之紀念日及民俗節日(0-2)計時30元，(2-19)計時20元，(19-24)計時30元</detail><datetime>2011-01-19T16:05:17.886466</datetime><geopt>25.08583,121.52113</geopt><address>台北市士林區前港街45號</address><total>535</total></parking><parking><name>成淵高中地下停車場</name><space>5</space><price>30/1小時</price><detail>全日月票5760元，計時30元，夜間優惠月票2400元</detail><datetime>2010-12-28T07:56:21.560749</datetime><geopt>25.061357,121.51866</geopt><address>台北大同區承德路二段235號之1號</address><total>275</total></parking><parking><name>TAIPEI 101</name><space>667</space><price>50/1小時</price><detail>汽車每小時收費50元，機車每小時收費20元</detail><datetime>2010-12-28T08:30:42.236633</datetime><geopt>25.033267,121.563705</geopt><address>台北信義區市府路台北101</address><total>1281</total></parking><parking><name>中坡公園地下停車場</name><space>176</space><price>30元/1小時 </price><detail>全日月票7200元，夜間優惠月票3000元(限19-8)，周一至周五(10-24)計時30元，(24-10)計時10元，周六至周日及政府行政機關放假之紀念日及民俗節日(10-12)計時30元，(12-24)計時40元，(24-10)計時10元</detail><datetime>2011-01-19T16:05:18.199090</datetime><geopt>25.046627,121.58044</geopt><address>台北市信義區中坡北路57號</address><total>213</total></parking><parking><name>民權公園地下停車場</name><space>102</space><price>30元/1小時</price><detail>全日月票5250元，計時30元，日間優惠月票2800元(7-19)，夜間優惠(22-8)計時10元</detail><datetime>2011-01-19T16:05:18.506437</datetime><geopt>25.061612,121.557972</geopt><address>台北市松山區民權東路四段180號</address><total>720</total></parking><parking><name>金華公園地下停車場</name><space>11</space><price>30元/1小時 六日40/1小時</price><detail>全日促銷月票5760元，里民優惠月票4600元，周一至周五(8-21)計時30元，(21-8)計時10元，周六至周日及政府行政機關放假之紀念日及民俗節日(8-21)計時40元，(21-8)計時10元</detail><datetime>2011-01-19T16:05:18.903657</datetime><geopt>25.029526,121.531647</geopt><address>市大安區金華街254巷1號</address><total>197</total></parking><parking><name>古亭國中地下停車場</name><space>35</space><price>30元/1小時</price><detail>全日月票4800元，計時30元，夜間月票2400元(18-8)</detail><datetime>2011-01-19T16:05:19.185548</datetime><geopt>25.024418,121.510551</geopt><address>台北市萬華區中華路二段606巷1號 </address><total>256</total></parking><parking><name>八德立體停車場</name><space>223</space><price>30元/1小時</price><detail>全月月票4800元，日間月票2000元(8-18)，夜間月票1200元(21-8)，周一至周四(8-24)計時30元，(0-8)計時10元；周五至周日(0-8)計時10元，(8-18)計時30元；(18-24)計時40元</detail><datetime>2011-01-19T16:05:19.496427</datetime><geopt>25.0486,121.556008</geopt><address>台北松山區八德路4段568號</address><total>424</total></parking><parking><name>景華公園地下停車場</name><space>554</space><price>20元/1小時</price><detail>停車場所在里里民月票2688元(全日月票原價3840元x70﹪)全日優惠月票3000元，日間月票2400元(7-19)，夜間月票1500元(19-8)，計時20元，(18-8)計時10元</detail><datetime>2011-01-19T16:05:19.776549</datetime><geopt>24.995262,121.543784</geopt><address>台北文山區景華街55號</address><total>760</total></parking><parking><name>松山高中地下停車場</name><space>63</space><price>30元/1小時</price><detail>全日促銷優惠月票5760元，計時30元，里民優惠月票4600元，夜間折扣(20-8)計時10元</detail><datetime>2011-01-19T16:05:20.045969</datetime><geopt>25.044071,121.564824</geopt><address>台北市信義區基隆路一段156號</address><total>228</total></parking><parking><name>東湖國小地下停車場</name><space>27</space><price>30元/1小時</price><detail>91.10.16開始收費 ⊙計時30元，日間月票1800元(7-19)，夜間月票1800元(19-8)，全日優惠月票3600元，里民優惠月票2400元，夜間折扣計時20元(18-8)，機車月票300元，計次20元(本場無所在里里民7折優惠)，97.1.1起出售汽車雙月票</detail><datetime>2011-01-19T16:05:20.329838</datetime><geopt>25.068546,121.615697</geopt><address>台北市內湖區東湖路115之1號</address><total>358</total></parking><parking><name>大稻埕公園地下停車場</name><space>37</space><price>30元/1小時</price><detail>月票5760元，計時30元 夜間優惠月票2000元(19-8)，夜間優惠計時10元(19-8) 計費單位：停車時數未滿1小時者，以1小時計算收費。停車時數逾1小時以上，其超過之不滿1小時部分，如不逾30分鐘者，以半小時計算；如逾30分鐘者，仍以1小時計算收費。</detail><datetime>2011-01-19T16:05:20.661438</datetime><geopt>25.0583,121.510519</geopt><address>台北市大同區歸綏街243號B1樓</address><total>205</total></parking><parking><name>西湖公園地下停車場</name><space>22</space><price>20元/1小時</price><detail>計時20元，全日月票4800元</detail><datetime>2010-12-28T08:05:56.704770</datetime><geopt>25.0822707,121.5701176</geopt><address>台北市內湖區內湖路1段387巷38號</address><total>172</total></parking><parking><name>SJU</name><space>5555</space><price>30/半小時</price><datetime>2011-04-09T03:53:17.852817</datetime><geopt>25.22723,121.451337</geopt><address>淡金路四段499號</address><total>10</total></parking><parking><name>社園立體停車場</name><space>155</space><price>20/1小時</price><detail>全日月票3600元，計時20元，夜間優惠月票1800元(18-8) </detail><datetime>2010-12-29T18:46:37.757764</datetime><geopt>25.1255884,121.548418</geopt><address>台北士林區延平北路6段180號</address><total>280</total></parking><parking><name>捷運木柵機廠停車場</name><space>1</space><price>電詢</price><datetime>2010-12-28T07:28:26.245894</datetime><geopt>24.9929212,121.57125</geopt><address>臺北市文山區新光路2段19號</address><total>683</total></parking><parking><name>承德公園地下停車場</name><space>83</space><price>30元/1小時</price><detail>地下2層，24小時全自動電腦計時收費；採計時收費，費率詳現場公告，另售有月票。</detail><datetime>2010-12-28T07:36:58.461909</datetime><geopt>25.0889228,121.5232881</geopt><address> 	臺北市士林區基河路150號</address><total>177</total></parking><parking><name>進安公園地下停車場</name><space>13</space><price>20/1小時</price><detail>全日促銷月票4800元，日間優惠月票3600元(7-20)，夜間優惠月票2000元(20-7)，計時20元</detail><datetime>2010-12-28T07:49:36.862209</datetime><geopt>25.046113,121.537703</geopt><address>台北中山區八德路二段158號</address><total>151</total></parking><parking><name>南港國小地下停車場</name><space>180</space><price>20元/1小時</price><detail>地下2層，24小時全自動電腦計時收費；採計時收費，費率詳現場公告，另售有月票。</detail><datetime>2010-12-28T07:45:46.212063</datetime><geopt>25.0559754,121.6119828</geopt><address>臺北市南港區興東街59號B1</address><total>300</total></parking><parking><name>玉成國小地下停車場</name><space>84</space><price>20元/1小時</price><detail>地下3層，24小時全自動電腦計時收費；計時20元，夜間折扣計時10元(18-8)，全日月票2500元，所在里月票1750元，優惠里民月票2000元；進場車輛限高2.1米。</detail><datetime>2010-12-28T07:51:58.999297</datetime><geopt>25.0530744,121.5926464</geopt><address>臺北市南港區昆陽街23號</address><total>297</total></parking><parking><name>大豐公園地下停車場</name><space>30</space><price>20/1小時</price><detail>停車場所在里里民月票3360元(全日月票原價4800元x70﹪)全日月票3600元不限購買對象(7-19)計時20元(19-7)計時10元</detail><datetime>2010-12-28T07:58:11.016871</datetime><geopt>25.131129,121.503934</geopt><address>台北北投區大興街145號</address><total>241</total></parking><parking><name>湖興立體停車場</name><space>126</space><price>30元/1小時</price><detail>實施停車場出入口周邊服務半徑300公尺內設籍里民按全月月票八折優惠</detail><datetime>2010-12-28T08:01:26.102724</datetime><geopt>25.0935968,121.5940773</geopt><address>台北市內湖區成功路2段322號</address><total>257</total></parking><parking><name>興隆公園地下停車場</name><price>20元/1小時</price><detail>小車計時20元，全日月票及里民月票優惠促銷3000元，所在里月票優惠促銷2700元</detail><datetime>2011-04-08T16:51:29.480577</datetime><geopt>25.000594,121.551152</geopt><address>臺北市文山區仙岩路128號</address><total>260</total></parking>
</list>
"""
 

request = urllib2.Request('http://yanparking.appspot.com/rest/parking', xml_data)
urllib2.urlopen(request)

