from kerykeion import (
    KrInstance,
    CompositeAspects,
)

from .expected_composite_aspects import EXPECTED_ALL_ASPECTS, EXPECTED_RELEVANT_ASPECTS

class TestNatalAspects:
    def setup_class(self):
        self.first_subject = KrInstance("John", 1940, 10, 9, 10, 30, "Liverpool", "GB")
        self.second_subject = KrInstance("Yoko", 1933, 2, 18, 10, 30, "Tokyo", "JP")

        self.composite_relevant_aspects = CompositeAspects(self.first_subject, self.second_subject).get_relevant_aspects()
        self.composite_all_aspects = CompositeAspects(self.first_subject, self.second_subject).get_all_aspects()

        self.expected_relevant_aspects = EXPECTED_RELEVANT_ASPECTS
        self.expected_all_aspects = EXPECTED_ALL_ASPECTS
    def test_relevant_aspects_length(self):
        assert len(self.expected_relevant_aspects) == 43

    def test_relevant_aspects(self):
        for i, aspect in enumerate(self.expected_relevant_aspects):
            assert self.composite_relevant_aspects[i]["p1_name"] == aspect["p1_name"]
            assert round(self.composite_relevant_aspects[i]["p1_abs_pos"], 3) == round(aspect["p1_abs_pos"], 3)
            assert self.composite_relevant_aspects[i]["p2_name"] == aspect["p2_name"]
            assert round(self.composite_relevant_aspects[i]["p2_abs_pos"], 3) == round(aspect["p2_abs_pos"], 3)
            assert self.composite_relevant_aspects[i]["aspect"] == aspect["aspect"]
            assert round(self.composite_relevant_aspects[i]['orbit'], 3) == round(aspect['orbit'], 3)
            assert round(self.composite_relevant_aspects[i]["aspect_degrees"], 3) == round(aspect["aspect_degrees"], 3)
            assert self.composite_relevant_aspects[i]["color"] == aspect["color"]
            assert self.composite_relevant_aspects[i]["aid"] == aspect["aid"]
            assert round(self.composite_relevant_aspects[i]["diff"], 3) == round(aspect["diff"], 3)
            assert self.composite_relevant_aspects[i]["p1"] == aspect["p1"]
            assert self.composite_relevant_aspects[i]["p2"] == aspect["p2"]

    def test_all_aspects_length(self):
        assert len(self.expected_all_aspects) == 64

    def test_all_aspects(self):
        for i, aspect in enumerate(self.expected_all_aspects):
            assert self.composite_all_aspects[i]["p1_name"] == aspect["p1_name"]
            assert round(self.composite_all_aspects[i]["p1_abs_pos"], 3) == round(aspect["p1_abs_pos"], 3)
            assert self.composite_all_aspects[i]["p2_name"] == aspect["p2_name"]
            assert round(self.composite_all_aspects[i]["p2_abs_pos"], 3) == round(aspect["p2_abs_pos"], 3)
            assert self.composite_all_aspects[i]["aspect"] == aspect["aspect"]
            assert round(self.composite_all_aspects[i]['orbit'], 3) == round(aspect['orbit'], 3)
            assert round(self.composite_all_aspects[i]["aspect_degrees"], 3) == round(aspect["aspect_degrees"], 3)
            assert self.composite_all_aspects[i]["color"] == aspect["color"]
            assert self.composite_all_aspects[i]["aid"] == aspect["aid"]
            assert round(self.composite_all_aspects[i]["diff"], 3) == round(aspect["diff"], 3)
            assert self.composite_all_aspects[i]["p1"] == aspect["p1"]
            assert self.composite_all_aspects[i]["p2"] == aspect["p2"]