import math
import random


def is_number(n):
    try:
        int(n)
    except ValueError:
        return False
    return True


def mae(predicts, targets, sample):
    total = 0
    for i in range(sample):
        loss = abs(predicts[i] - targets[i])
        print(f"loss name: MAE, sample: {i}, pred: {
              predicts[i]}, target: {targets[i]}, loss: {loss}")
        total += loss
    print(f"final MAE: {total / sample}")


def mse(predicts, targets, sample):
    total = 0
    for i in range(sample):
        loss = (predicts[i] - targets[i]) ** 2
        print(f"loss name: MSE, sample: {i}, pred: {
              predicts[i]}, target: {targets[i]}, loss: {loss}")
        total += loss
    print(f"final MSE: {total / sample}")


def rmse(predicts, targets, sample):
    total = 0
    for i in range(sample):
        loss = (predicts[i] - targets[i]) ** 2
        print(f"loss name: RMSE, sample: {i}, pred: {
              predicts[i]}, target: {targets[i]}, loss: {loss}")
        total += loss
    print(f"final RMSE: {math.sqrt(total / sample)}")


def regression_loss():
    sample = input(
        'Input number of samples (integer number) which are generated: ')
    if not is_number(sample):
        print('Number of samples must be an integer number.')
        return

    sample = int(sample)
    loss_functions = ['MAE', 'MSE', 'RMSE']

    loss_name = input('Input loss name (MAE | MSE | RMSE): ')

    if loss_name not in loss_functions:
        print(f'{loss_name} is not a supported loss function.')
        return

    # Generate samples randomly
    predicts = [random.uniform(0.0, 10.0) for _ in range(sample)]
    targets = [random.uniform(0.0, 10.0) for _ in range(sample)]

    if loss_name == 'MAE':
        mae(predicts, targets, sample)
    elif loss_name == 'MSE':
        mse(predicts, targets, sample)
    else:
        rmse(predicts, targets, sample)


regression_loss()
