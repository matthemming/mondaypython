def ip_get_network(ip, snm):
	'''Inputs are an ip address and a subnet mask. 
	Must be supplied as strings
	Returns network id'''
	return '.'.join([str((int(ip.split('.')[i]) & int(snm.split('.')[i]))) for i in range(len(ip.split('.')))])
	
def ip_get_networks(snm, *ip):
	'''Inputs are a subnet mask and a list of ip addressess. 
	Must be supplied as strings
	Returns network ids'''
	networkids = []
	for i in ip:
		iplist = i.split('.')
		snmlist = snm.split('.')
		networkid = '.'.join([str((int(iplist[j]) & int(snmlist[j]))) for j in range(len(iplist))]) 
		networkids.append(networkid)
	return networkids

def get_network_by_ip_snm(**kwargs):
	'''Input is a dictionary of ip addressess and subnet masks
	in the form ip_address:subnet_mask. 
	Must be supplied as strings
	Returns network ids'''
	networkids = []
	for i, s in kwargs.items():
		iplist = i.split('.')
		snmlist = s.split('.')
		networkid = '.'.join([str((int(iplist[j]) & int(snmlist[j]))) for j in range(len(iplist))]) 
		networkids.append(networkid)
	return networkids