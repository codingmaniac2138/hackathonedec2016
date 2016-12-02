"""
PART-II

(ii) Write a program that reads a json file , performs following edits and store json back to the same file. update following fields -

A. Change firewall - protocol - from tcp to udp
B. Change 3rd vnics- portgroup name to EXT_VLAN_201b
C. Change ospf- enabled = false to true
D. Update holddowntimer = holddowntimer +keepalivetimer

"""
import json

with open('sample.json') as json_file:
#create an object of json file
    obj = json.load(json_file)

#access key value pairs and update the keyvalues
    obj["featureConfigs"]["features"][2]["firewallRules"]["firewallRules"][0]["application"]["service"][0]["protocol"] = "udp"
    obj["vnics"]["vnics"][2]["portgroupName"] = "EXT_VLAN_202b"
    obj["featureConfigs"]["features"][5]["ospf"]["enabled"] =True

#change the timer values at each place as asked
    holddowntimer_value = obj["featureConfigs"]["features"][5]["bgp"]["bgpNeighbours"]["bgpNeighbours"][0]["holdDownTimer"]
    keepalivetimer_value = obj["featureConfigs"]["features"][5]["bgp"]["bgpNeighbours"]["bgpNeighbours"][0]["keepAliveTimer"]

    timer = obj["featureConfigs"]["features"][5]["bgp"]["bgpNeighbours"]["bgpNeighbours"][0]
    test = obj["featureConfigs"]["features"][5]["bgp"]["bgpNeighbours"]["bgpNeighbours"]

    for i in test:
        i["holdDownTimer"]= i["holdDownTimer"] + i["keepAliveTimer"]

    with open("sample.json", "w") as file:
        file.write(json.dumps(obj, file, indent=4))


