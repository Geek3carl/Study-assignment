#!/usr/bin/env python3
import sys
import os
zonecode = {
	'广东省':
		{'广州市':['越秀区','海珠区','荔湾区','天河区'],
		'深圳市':['宝安区','龙岗区','南山区','盐田区','罗湖区','福田区'],
		'珠海市':['香洲区','斗门区','金湾区'],
		'汕头市':['潮阳区','澄海区','濠江区','龙湖区']},
	'湖北省':
		{'武汉市':['江岸区','江汉区','汉阳区','武昌区','洪山区','青山区'],
		'黄石市':['黄石港区','西塞山区','下陆区','铁山区'],
		'十堰市':['张湾区','茅箭区','竹山县','竹溪县'],
		'荆州市':['荆州区','沙市区','江陵县','监利县','公安县']},
	'福建省':
		{'福州市':['鼓楼区','台江区','仓山区','马尾','晋安区','琅岐区'],
		'厦门市':['同安区','翔安区','集美区','海沧区','湖里区','思明区'],
		'莆田市':['仙游县','荔城区','城厢区','涵江区','秀屿区'],
		'三明市':['梅列区','三元区','永安市','明溪县','清流县','宁化县']},
	'吉林省':
		{'长春市':['朝阳区','南关区','宽城区','二道区','绿园区','双阳区','德惠市','九台市','榆树市','农安县'],
		'吉林市':['船营区','龙潭区','昌邑区','丰满区','磐石市','蛟河市','桦甸市','舒兰市','永吉县'],
		'四平市':['铁西区','铁东区','双辽市','公主岭市','梨树县','伊通满族自治县'],
		'辽源市':['龙山区','西安区','东丰县','东辽县'],
		'通化市':['东昌区','二道江区','梅河口市','集安市','通化县','柳河县','辉南县',],
		'白山市':['八道江区','临江市','江源县','抚松县','靖宇县','长白朝鲜族自治区',],
		'松原市':['宁江区','扶余县','长岭县','乾安县','前郭尔罗斯蒙古族自治区',],
		'白城市':['洮北区','大安区','洮南市','通榆县','镇赉县',]},
		}
#循环开始
for a in zonecode:
	print(a)
while True:
    input_name = input("请输入您要查看的省（q可退出）：")
    if input_name=='q':
        sys.exit()
    elif input_name in zonecode.keys():    #正确判断
        sheng = zonecode[input_name]
        for shurua in sheng:
              print(shurua)
	#第二层循环
        while True:
            city_name = input("请输入您要查看的市（b可返回上级，q可退出）：")
            if city_name=='q':
                sys.exit()
            elif city_name=='b':
                break
            elif city_name in  zonecode[input_name].keys():
                shi = zonecode[input_name][city_name]
                for shurub in shi:
                    print(shurub)
				#第三层循环
                while  True:
                    try:
                        part_name= input("请输入您要查看的区（b可返回上级，q可退出）：")
                        if part_name=='q':
                            sys.exit()
                        elif part_name=='b':
                           break
                    except Keyrror:
                         print("您的输入有误，请重新输入")
                    else:
                        if part_name  in zonecode[input_name][city_name]:
                            print(part_name)
                    break
            else:
                print("您的输入有误，请重新输入")
            break  
    else:
         print("您的输入有误，请重新输入")
         continue
    break