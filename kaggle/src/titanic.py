from core import pd, path
pd.set_option('future.no_silent_downcasting', True)

class Titanic:
    COLS = ['PassengerId', 'Sex', 'Age', 
            'SibSp', 'Parch', 'Fare', 'Embarked']
    TARGET = ['Survived']
    def __init__(self):
        path_data = path / 'data/titanic'
        train_data = pd.read_csv(path_data / 'train.csv')[Titanic.COLS + Titanic.TARGET]
        test_data  = pd.read_csv(path_data / 'test.csv' )[Titanic.COLS]
        #
        self.train_data = self.__cure(train_data)
        self.test_data  = self.__cure(test_data)
        breakpoint()
    #
    def __cure(self, df):
        replace = {
            'Sex': {'male': 0, 'female': 1},
            'Embarked': {'S': 0, 'C': 1, 'Q': 2}
         }
        #
        df_rep = df.assign(
            **{k:df[k].replace(x).astype(float) for k, x in replace.items()}
        )
        return df_rep