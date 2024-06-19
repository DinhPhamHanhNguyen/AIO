def model_evaluation(tp, fp, fn):
    # checking whether tp, fp, fn are integer or not
    if not isinstance(tp, int):
        print("tp must be int")
        return

    if not isinstance(fp, int):
        print("fp must be int")
        return

    if not isinstance(fn, int):
        print("fn must be int")
        return
    # Checking whether tp, fp, fn are greater than 0 or not
    if tp <= 0 or fp <= 0 or fn <= 0:
        print("tp and fp and fn must be greaterthanzero")
        return

    precision = tp/(tp+fp)
    recall = tp/(tp + fn)
    F1_score = 2 * (precision * recall)/(precision+recall)

    print(f'precision is {precision}')
    print(f'recall is {recall}')
    print(f'f1_score is {F1_score}')


model_evaluation(2, 3, 4)
model_evaluation('a', 3, 4)
model_evaluation(2, 'a', 4)
model_evaluation(2, 3, 'a')
model_evaluation(2, 3, 0)
model_evaluation(2.1, 3, 0)
