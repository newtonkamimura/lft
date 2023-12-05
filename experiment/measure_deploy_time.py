from experiment.deploy_lft import DeployLFT
from time import time, sleep
from time import time, sleep
from experiment.deploy_mininet import DeployMininet


dmn = DeployMininet()
nodes = 250
mnDeployTime = {}
mnUeployTime = {}


for i in range(100):
        start = time()
        dmn.deploy(i)
        mnDeployTime[i] = time() - start
        sleep(3)
        start = time()
        dmn.undeploy()
        mnUndeployTime[i] = time() - start
        sleep(3)


print(mnDeployTime)
print(mnUndeployTime)


dlft = DeployLFT()
lftDeployTime = {}
lftUndeployTime = {}


for i in range(nodes):
	start = time()
	dlft.deploy(i)
	end = time()
	lftDeployTime[i] = end-start
	dlft.getReferences(i)
	sleep(3)
	start = time()
	dlft.undeploy()
	end = time()
	lftUndeployTime[i] = end-start
	sleep(3)

print(lftDeployTime)
print(lftUndeployTime)
