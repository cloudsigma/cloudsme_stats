import json
import cloudsigma
import sys


if len(sys.argv) <= 1:
    print >>sys.stderr, "Pass the config file as the first argument. \n" \
          "Here is an example template for a config file. Please specify account email, password and cloud location:"
    print >>sys.stderr, """
    {
        "alias_one": {"username": "user@company.com", "password": "secret", "api_endpoint":"https://wdc.cloudsigma.com/api/2.0/"},
        "alias_two": {"username": "another@company.com", "password": "secret2", "api_endpoint":"https://wdc.cloudsigma.com/api/2.0/"}
    }
    """
    sys.exit(-1)

users = json.load(open(sys.argv[1], 'r'))

metrics = {
    'MemoryUsage': {},
    'NumberOfUsedCPUCores': {},
    'NumberOfVMImages': {},
    'NumberOfVirtualMachines': {},
}

for alias, user in users.iteritems():
    started_servers = [server for server in cloudsigma.resource.Server(**user).list_detail() if server['status'] == 'running']
    drives = cloudsigma.resource.Drive(**user).list()
    metrics['MemoryUsage'][alias] = sum(guest['mem'] for guest in started_servers)
    metrics['NumberOfUsedCPUCores'][alias] = sum(guest['smp'] for guest in started_servers)
    metrics['NumberOfVirtualMachines'][alias] = len(started_servers)
    metrics['NumberOfVMImages'][alias] = len(drives)

dump = {
    'Cloud name': 'CloudSigma',
    'Metrics': metrics,
}

print json.dumps(dump, indent=True)
