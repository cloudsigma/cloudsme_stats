# Client tool for collecting statistics from multiple accounts #

Create a config file e.g. named `conf.json` with the following contents:

    {
        "alias_one": {"username": "user@company.com", "password": "secret", "api_endpoint":"https://wdc.cloudsigma.com/api/2.0/"},
        "alias_two": {"username": "another@company.com", "password": "secret2", "api_endpoint":"https://wdc.cloudsigma.com/api/2.0/"}
    }

Please verify the accounts are pointed to the right cloud location URL. Here is a list of the current cloud location API endpoints:

 * https://wdc.cloudsigma.com/api/2.0/
 * https://lvs.cloudsigma.com/api/2.0/
 * https://zrh.cloudsigma.com/api/2.0/

Then you can invoke the stats collection using the command:

    $ cloudsigma_stats conf.json
    {
     "Metrics": {
      "NumberOfVirtualMachines": {
       "alias_one": 0,
       "alias_two": 0
      },
      "NumberOfUsedCPUCores": {
       "alias_one": 0,
       "alias_two": 0
      },
      "MemoryUsage": {
       "alias_one": 0,
       "alias_two": 0
      },
      "NumberOfVMImages": {
       "alias_one": 1,
       "alias_two": 0
      }
     },
     "Cloud name": "CloudSigma"
    }

If the exit code of the command is 0, the standard output will contain a valid JSON output.

If the `cloudsigma_stats` command is executed without parameters, it prints a template for the config file.

If any error occurs (invalid config file, wrong URL, wrong credentials, problem with connection), the command
will exit with non-zero return code and will print an error trace on the standard output.
