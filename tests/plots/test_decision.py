import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as pl
import numpy as np
import shap


def test_random_decision():
    shap.dependence_plot(0, np.random.randn(20, 5), np.random.randn(20, 5), show=False)
    pl.close()

# ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##
#
# Visual tests
#
# ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##

# import lightgbm as lgb
# import matplotlib.pyplot as pl
# import numpy as np
# from scipy.special import expit
# from sklearn.model_selection import train_test_split
#
# import shap
#
# random_state = 7
#
# X, y = shap.datasets.adult()
# X_display, y_display = shap.datasets.adult(display=True)
#
# # create a train/test split
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=random_state)
# d_train = lgb.Dataset(X_train, label=y_train)
# d_test = lgb.Dataset(X_test, label=y_test)
#
# params = {
#     "max_bin": 512,
#     "learning_rate": 0.05,
#     "boosting_type": "gbdt",
#     "objective": "binary",
#     "metric": "binary_logloss",
#     "num_leaves": 10,
#     "verbose": -1,
#     "min_data": 100,
#     "boost_from_average": True,
#     "random_state": random_state
# }
#
# model = lgb.train(params, d_train, 1000, valid_sets=[d_test], early_stopping_rounds=50, verbose_eval=False)
#
# explainer = shap.TreeExplainer(model)
# base_value = explainer.expected_value
# select = range(20)
# features = X_test.iloc[select]
# y_label = y_test[select]
# shap_values = explainer.shap_values(features)
# shap_interaction_values = explainer.shap_interaction_values(features)
# features_display = X_display.loc[features.index]
#
# args1 = dict(base_value=base_value, shap_values=shap_values, matplotlib=True)
# args2 = args1.copy()
# args2["shap_values"] = shap_interaction_values
#
# # ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##
# # Basic plots with default (importance) sort and generated labels.
# # ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##
#
# shap.decision_plot(**args1)
# shap.decision_plot(**args2)
#
# shap.decision_plot(highlight=[0, 9], **args1)
#
# shap.decision_plot(features=features_display, **args1)
# shap.decision_plot(features=features_display, **args2)
#
# # Plot a single observation without features
# shap.decision_plot(base_value, shap_values[0, :], matplotlib=True)
# shap.decision_plot(base_value, shap_values[[0], :], matplotlib=True)
#
# # Now, with a Pandas Series (and also test auto feature value positioning)
# shap.decision_plot(base_value, shap_values[0, :], features=features_display.iloc[0, :], matplotlib=True)
# s = shap_values[0, :].copy()
# s[-1] = -35; s[-2] = 15
# shap.decision_plot(base_value, s, features=features_display.iloc[0, :], matplotlib=True, feature_order='None')
# s[-1] = 40; s[-2] = -20
# shap.decision_plot(base_value, s, features=features_display.iloc[0, :], matplotlib=True, feature_order='None')
# shap.decision_plot(base_value, shap_values[4, :], features=features_display.iloc[4, :], feature_order='hclust', matplotlib=True)
# shap.decision_plot(base_value, shap_values[7, :], features=features_display.iloc[7, :], feature_order='hclust', matplotlib=True)
# shap.decision_plot(base_value, shap_interaction_values[[0], :], features=features_display.iloc[0, :], matplotlib=True)
# # Now with a single observation using a matrix and a Pandas Dataframe
# shap.decision_plot(base_value, shap_values[[0], :], features=features_display.iloc[[0], :], matplotlib=True)
# shap.decision_plot(base_value, shap_interaction_values[[0], :], features=features_display.iloc[[0], :], matplotlib=True)
# # Now with feature names in the features argument.
# names = features_display.columns.to_list()
# shap.decision_plot(base_value, shap_values[[0], :], features=names, matplotlib=True)
# shap.decision_plot(base_value, shap_interaction_values[[0], :], features=names, matplotlib=True)
# # Now with feature names in the features argument as numpy.
# shap.decision_plot(base_value, shap_values[[0], :], features=np.array(names), matplotlib=True)
# shap.decision_plot(base_value, shap_interaction_values[[0], :], features=np.array(names), matplotlib=True)
#
# names = features_display.columns.to_list()
# args1["feature_names"] = names
# args2["feature_names"] = names
#
# # Plot font changes sizes depending on whether an interaction feature is printed.
# shap.decision_plot(feature_display_range=slice(None, -11, -1), **args2)
# shap.decision_plot(feature_display_range=slice(None, -9, -1), **args2)
#
# # Highlighting by index
# highlight = [1, 9]
# shap.decision_plot(highlight=highlight, **args1)
#
# # Highlighting by boolean array
# predictions = base_value + shap_values.sum(1)
# highlight = np.abs(predictions) > 9
# shap.decision_plot(highlight=highlight, **args1)
# highlight = y_label != (expit(predictions) > 0.5)
# shap.decision_plot(highlight=highlight, **args1)
#
# # Highlighting by slice
# shap.decision_plot(highlight=slice(0, 10), **args1)
#
# # Logit link
# shap.decision_plot(link="logit", **args1)
# shap.decision_plot(link="logit", **args2)
#
# # Color scheme
# shap.decision_plot(plot_color="coolwarm", **args1)
#
# # Axis color
# shap.decision_plot(axis_color="#FF0000", **args1)
#
# # Y feature demarcation color
# shap.decision_plot(y_demarc_color="#FF0000", **args1)
#
# # Alpha value
# shap.decision_plot(alpha=0.2, **args1)
#
# # Disable color bar
# shap.decision_plot(color_bar=False, **args1)
# shap.decision_plot(color_bar=False, feature_display_range=slice(-20, None, 1), **args1)
#
# # Disable autosize
# shap.decision_plot(auto_size_plot=False, **args1)
# shap.decision_plot(auto_size_plot=False, **args2)
#
# # Enable title
# shap.decision_plot(title="This doesn't look good", **args1)
#
# # Disable show
# shap.decision_plot(show=False, **args1)
# pl.show()
#
# # Flip y-axis
# shap.decision_plot(feature_display_range=slice(-20, None, 1), **args1)
# shap.decision_plot(feature_display_range=slice(-20, None, 1), **args2)
# shap.decision_plot(**args2) # to compare with previous plot
#
# # Use return_objects
# r = shap.decision_plot(return_objects=True, **args1)
# idx = 8
# shap.decision_plot(base_value, shap_values[idx], features=features_display.iloc[idx],
#                    feature_order=r.feature_idx, xlim=r.xlim, matplotlib=True)
#
#
# # ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##
# # No sorting
# # ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##
#
# shap.decision_plot(feature_order="none", **args1)
# shap.decision_plot(feature_order="none", feature_display_range=slice(-20, None, 1), **args1)
# shap.decision_plot(feature_order="none", **args2)
# shap.decision_plot(feature_order="none", feature_display_range=slice(-20, None, 1), **args2)
# shap.decision_plot(feature_order=None, **args1)
# shap.decision_plot(feature_order=None, **args2)
#
#
# # ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##
# # Hierarchical cluster sorting
# # ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##
#
# shap.decision_plot(feature_order="hclust", **args1)
# shap.decision_plot(feature_order="hclust", feature_display_range=slice(-20, None, 1), **args1)
# shap.decision_plot(feature_order="hclust", **args2)
# shap.decision_plot(feature_order="hclust", feature_display_range=slice(-20, None, 1), **args2)
#
#
# # ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##
# # Feature display range
# # ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##
#
# shap.decision_plot(**args1)
# r = shap.decision_plot(feature_display_range=range(0, 20), return_objects=True, **args1)
# shap.decision_plot(feature_display_range=range(0, 1), xlim=r.xlim, **args1)
# shap.decision_plot(feature_display_range=range(0, 2), xlim=r.xlim, **args1)
# shap.decision_plot(feature_display_range=range(1, 2), xlim=r.xlim, **args1)
# shap.decision_plot(feature_display_range=range(10, 12), xlim=r.xlim, **args1)
# shap.decision_plot(feature_display_range=range(11, 9, -1), xlim=r.xlim, **args1)
# shap.decision_plot(feature_display_range=range(11, 12), xlim=r.xlim, **args1)
# shap.decision_plot(feature_display_range=range(11, 10, -1), xlim=r.xlim, **args1)
# shap.decision_plot(feature_display_range=range(11, 0, -1), xlim=r.xlim, **args1)
#
# shap.decision_plot(feature_display_range=slice(1), xlim=r.xlim, **args1)
# shap.decision_plot(feature_display_range=slice(-12, -13, -1), xlim=r.xlim, **args1)
# shap.decision_plot(feature_display_range=slice(0, 2), xlim=r.xlim, **args1)
# shap.decision_plot(feature_display_range=slice(-11, -13, -1), xlim=r.xlim, **args1)
#
# shap.decision_plot(feature_order='hclust', feature_display_range=slice(None, -21, -1), xlim=r.xlim, **args2)
# shap.decision_plot(feature_order='hclust', feature_display_range=slice(20, None, -1), xlim=r.xlim, **args2)
#
# # decision_plot transforms negative values in a range so they are interpreted correctly in a slice.
# shap.decision_plot(feature_order='hclust', feature_display_range=range(11, -1, -1), xlim=r.xlim, **args2)
# shap.decision_plot(feature_order='hclust', feature_display_range=range(-100, 12, 1), xlim=r.xlim, **args2)
#
#
