#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# This file is auto-generated by h2o-3/h2o-bindings/bin/gen_python.py
# Copyright 2016 H2O.ai;  Apache License Version 2.0 (see LICENSE for details)
#
from __future__ import absolute_import, division, print_function, unicode_literals

from h2o.estimators.estimator_base import H2OEstimator
from h2o.exceptions import H2OValueError
from h2o.frame import H2OFrame
from h2o.utils.typechecks import assert_is_type, Enum, numeric


class H2OAggregatorEstimator(H2OEstimator):
    """
    Aggregator

    """

    algo = "aggregator"

    def __init__(self, **kwargs):
        super(H2OAggregatorEstimator, self).__init__()
        self._parms = {}
        names_list = {"model_id", "training_frame", "response_column", "ignored_columns", "ignore_const_cols",
                      "radius_scale", "transform", "categorical_encoding"}
        if "Lambda" in kwargs: kwargs["lambda_"] = kwargs.pop("Lambda")
        for pname, pvalue in kwargs.items():
            if pname == 'model_id':
                self._id = pvalue
                self._parms["model_id"] = pvalue
            elif pname in names_list:
                # Using setattr(...) will invoke type-checking of the arguments
                setattr(self, pname, pvalue)
            else:
                raise H2OValueError("Unknown parameter %s = %r" % (pname, pvalue))

    @property
    def training_frame(self):
        """str: Id of the training data frame (Not required, to allow initial validation of model parameters)."""
        return self._parms.get("training_frame")

    @training_frame.setter
    def training_frame(self, training_frame):
        assert_is_type(training_frame, None, H2OFrame)
        self._parms["training_frame"] = training_frame


    @property
    def response_column(self):
        """str: Response variable column."""
        return self._parms.get("response_column")

    @response_column.setter
    def response_column(self, response_column):
        assert_is_type(response_column, None, str)
        self._parms["response_column"] = response_column


    @property
    def ignored_columns(self):
        """List[str]: Names of columns to ignore for training."""
        return self._parms.get("ignored_columns")

    @ignored_columns.setter
    def ignored_columns(self, ignored_columns):
        assert_is_type(ignored_columns, None, [str])
        self._parms["ignored_columns"] = ignored_columns


    @property
    def ignore_const_cols(self):
        """bool: Ignore constant columns. (Default: True)"""
        return self._parms.get("ignore_const_cols")

    @ignore_const_cols.setter
    def ignore_const_cols(self, ignore_const_cols):
        assert_is_type(ignore_const_cols, None, bool)
        self._parms["ignore_const_cols"] = ignore_const_cols


    @property
    def radius_scale(self):
        """float: Radius scaling (Default: 1.0)"""
        return self._parms.get("radius_scale")

    @radius_scale.setter
    def radius_scale(self, radius_scale):
        assert_is_type(radius_scale, None, numeric)
        self._parms["radius_scale"] = radius_scale


    @property
    def transform(self):
        """
        Enum["none", "standardize", "normalize", "demean", "descale"]: Transformation of training data (Default:
        "normalize")
        """
        return self._parms.get("transform")

    @transform.setter
    def transform(self, transform):
        assert_is_type(transform, None, Enum("none", "standardize", "normalize", "demean", "descale"))
        self._parms["transform"] = transform


    @property
    def categorical_encoding(self):
        """
        Enum["auto", "enum", "one_hot_internal", "one_hot_explicit", "binary", "eigen"]: Encoding scheme for categorical
        features (Default: "auto")
        """
        return self._parms.get("categorical_encoding")

    @categorical_encoding.setter
    def categorical_encoding(self, categorical_encoding):
        assert_is_type(categorical_encoding, None, Enum("auto", "enum", "one_hot_internal", "one_hot_explicit", "binary", "eigen"))
        self._parms["categorical_encoding"] = categorical_encoding


