import wandb

# start a new wandb run to track this script
def wandb_init(project="DRL_Gym_PyTorch", extra_config=None):
    # group must be last in the config here (pop).
    config = {"dataset": "GridWorld", "epochs": None, "group": "default"}
    for key, value in extra_config.items():
        config[key] = value
    group_value = config["group"]
    del config["group"]

    wandb.init(
        # set the wandb project where this run will be logged
        project=project,
        # track hyperparameters and run metadata
        config=config,
        group=group_value
    )