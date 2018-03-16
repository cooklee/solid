import pandas as pd
from src.obtain import get_clean_data
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.externals import joblib


def crate_two_models(data_frame):

    X = data_frame.copy().drop(['iris_type'], axis=1).values
    y = data_frame.copy().loc[:, 'iris_type'].replace({'setosa': 0, 'versicolor': 1, 'virginica': 2}).values
    X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2)

    lr_0 = LogisticRegression()
    lr_0.fit(X_tr, y_tr)
    y_pr = lr_0.predict(X_te)
    accuracy_score(y_te, y_pr)
    joblib.dump(lr_0, '/home/models/logistic.pkl')


    X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.3)

    dt_0 = DecisionTreeClassifier()
    dt_0.fit(X, y)
    y_pr = dt_0.predict(X_te)

    accuracy_score(y_te, y_pr)
    joblib.dump(dt_0, '/home/models/model-tree.pkl')


