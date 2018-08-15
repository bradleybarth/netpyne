from netpyne import specs
from netpyne.batch import Batch 

def dentateGyrus():
	# create Batch object with paramaters to modify, and specifying files to use
	dGyrus = Batch(cfgFile='simConfig.py', netParamsFile='netParams.py')
	
	# Set output folder, grid method (all param combinations), and run configuration
	dGyrus.batchLabel = 'dentateGyrus'
	dGyrus.method = 'evolutionary_algorithm_with_gcp'
	dGyrus.runCfg = {
		'batch': {
			'script': 'init.py',
			'mpiCommand': 'mpiexec',
			'numproc': 2,
			'paramNames': ['prob', 'weight', 'delay'],
		},
		'evolve': {
			'pop_size': 40,
			'num_elites': 2, # keep this number of parent for next generation
			'maximize': False, # maximize fitnes function?
			'mutation_rate': 0.2,
			'max_generations': 1000,
			'mutation_strength': 0.65, # <1 mutation is close to original. >1 mutation is far from original. 
			'upper_bound' : [0.5,   0.1,   20], # upper value limit for param 1, 2, ...
			'lower_bound' : [0.01,  0.001,  1], # lower value limit for param 1, 2, ...
			'fitness': 'abs(17 - float(len(sim.simData["spkt"])) / 40)', # fitness extression. shoud read simData
			'time_sleep': 5, # wait this time before checking again if sim is completed (for each generation)
			'maxiter_wait': 5000, # max number of times to check if sim is completed (for each generation)
			'default_fitness': -1 # set fitness value in case simulation time is over
		},
		'SBATCH': {
			'--account': 'myUser',
			'--nodes': 1,
			'--ntasks-per-node': 8,
			'--mail-user': 'abc@gmil.com',
			'--mail-type': 'none',
			'--time': '00:05:00',
			'--output': '.run',
			'--error': '.error',
		},
		'bash': {
			'reservation': '',
			'custom': ''
		}
	}
	# Run batch simulations
	dGyrus.run()

# Main code
if __name__ == '__main__':
	dentateGyrus() 
