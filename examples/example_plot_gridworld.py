import sys
sys.path.append("..")
import numpy as np
from env.grid_world import GridWorld
from utils.plots import plot_gridworld

###########################################################
#          Plot a grid world with no solution             #
###########################################################

# specify world parameters
num_cols = 10
num_rows = 10
obstructions = np.array([[0,7],[1,1],[1,2],[1,3],[1,7],[2,1],[2,3],
                         [2,7],[3,1],[3,3],[3,5],[4,3],[4,5],[4,7],
                         [5,3],[5,7],[5,9],[6,3],[6,9],[7,1],[7,6],
                         [7,7],[7,8],[7,9],[8,1],[8,5],[8,6],[9,1]])
bad_states = np.array([[1,9],[4,2],[4,4],[7,5],[9,9]])
restart_states = np.array([[3,7],[8,2]])
start_state = np.array([[0,4]])
goal_states = np.array([[0,9],[2,2],[8,7]])

# create model
gw = GridWorld(num_rows=num_rows,
               num_cols=num_cols,
               start_state=start_state,
               goal_states=goal_states)
gw.add_obstructions(obstructed_states=obstructions,
                    bad_states=bad_states,
                    restart_states=restart_states)
gw.add_rewards(step_reward=-1,
               goal_reward=10,
               bad_state_reward=-6,
               restart_state_reward=-10)
gw.add_transition_probability(p_good_transition=0.7,
                              bias=0.5)
gw.add_discount(discount=0.9)
model = gw.create_gridworld()

# plot world
path = "../doc/imgs/unsolved_gridworld.png"
plot_gridworld(model, title="Test world", path=path)

# [added]
from examples.example_value_iteration import value_iteration
# solve with value iteration
value_function, policy = value_iteration(model, maxiter=100)

# plot the results
plot_gridworld(model, value_function=value_function, policy=policy, title="Value iteration")