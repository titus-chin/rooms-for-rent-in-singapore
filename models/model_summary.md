# Model Summary

## Hyperparameters Tuning
Hyperparameters to be tuned for each model.

| Models                   | Hyperparameters                     | Values                                 |
| ------------------------ | ----------------------------------- | -------------------------------------- |
| DummyClassifier          | random_state                        | 0                                      |
|                          | strategy                            | uniform, maximum                       |
| Model 2                  | -                                   | -                                      |

## Best Hyperparameters of Each Model
Best hyperparameters of each model based on validation accuracy. Details of hyperparameters tuning can be found on [Weights & Biases dashboard]().

| Models                   | Best Hyperparameters                | Validation Accuracy                    |
| ------------------------ | ----------------------------------- | -------------------------------------- |
| DummyClassifier          | random_state = 0                    | 53%                                    |
|                          | strategy = uniform                  |                                        |
| KNeighborsClassifier     | k = 10                              | 83%                                    |
| Model 3                  | -                                   | -                                      |

## Performance of Each Model
Train each model with its best hyperparameters, and get its training and testing accuracy.

| Models                   | Training Accuracy                   | Testing Accuracy                       |
| ------------------------ | ----------------------------------- | -------------------------------------- |
| DummyClassifier          | 55%                                 | 53%                                    |
| KNeighborsClassifier     | 85%                                 | 83%                                    |
| Model 3                  | -                                   | -                                      |

## Best Performing Model
KNeighborsClassifier is the best performing model because...