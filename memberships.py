import numpy as np
import skfuzzy as fuzz

from skfuzzy import control as ctrl
from categories import land_use, land_form, slope_ctgr, impervious_ctgr


class Memberships:

    def __init__(self):
        self.land_use_type = ctrl.Antecedent(np.arange(0, 10, 1), 'land_use')
        self.land_form_type = ctrl.Antecedent(np.arange(0, 14, 1), 'land_form')
        self.slope = ctrl.Consequent(np.arange(1, 101, 1), 'slope')
        self.impervious = ctrl.Consequent(np.arange(1, 101, 1), 'impervious')
        
    def populate_land_use(self):
        # Populate land use type with membership functions.
        self.land_use_type[land_use.marshes_and_lowlands] = fuzz.trimf(self.land_use_type.universe, [0, 1, 2])
        self.land_use_type[land_use.flats_and_plateaus] = fuzz.trimf(self.land_use_type.universe, [1, 2, 3])
        self.land_use_type[land_use.flats_and_plateaus_in_combination_with_hills] = fuzz.trimf(self.land_use_type.universe, [2, 3, 4])
        self.land_use_type[land_use.hills_with_gentle_slopes] = fuzz.trimf(self.land_use_type.universe, [3, 4, 5])
        self.land_use_type[land_use.steeper_hills_and_foothills] = fuzz.trimf(self.land_use_type.universe, [4, 5, 6])
        self.land_use_type[land_use.hills_and_outcrops_of_mountain_ranges] = fuzz.trimf(self.land_use_type.universe, [5, 6, 7])
        self.land_use_type[land_use.higher_hills] = fuzz.trimf(self.land_use_type.universe, [6, 7, 8])
        self.land_use_type[land_use.mountains] = fuzz.trimf(self.land_use_type.universe, [7, 8, 9])
        self.land_use_type[land_use.highest_mountains] = fuzz.trimf(self.land_use_type.universe, [8, 9, 10])

    def populate_land_form(self):
        # Populate land form type with membership functions.
        self.land_form_type[land_form.medium_conditions] = fuzz.trimf(self.land_form_type.universe, [0, 1, 2])
        self.land_form_type[land_form.permeable_areas] = fuzz.trimf(self.land_form_type.universe, [1, 2, 3])
        self.land_form_type[land_form.permeable_terrain_on_plains] = fuzz.trimf(self.land_form_type.universe, [2, 3, 4])
        self.land_form_type[land_form.hilly_terrain] = fuzz.trimf(self.land_form_type.universe, [3, 4, 5])
        self.land_form_type[land_form.mountainous_terrain] = fuzz.trimf(self.land_form_type.universe, [4, 5, 6])
        self.land_form_type[land_form.bare_rocky_slopes] = fuzz.trimf(self.land_form_type.universe, [5, 6, 7])
        self.land_form_type[land_form.urban] = fuzz.trimf(self.land_form_type.universe, [6, 7, 8])
        self.land_form_type[land_form.suburban] = fuzz.trimf(self.land_form_type.universe, [7, 8, 9])
        self.land_form_type[land_form.rural] = fuzz.trimf(self.land_form_type.universe, [8, 9, 10])
        self.land_form_type[land_form.forests] = fuzz.trimf(self.land_form_type.universe, [9, 10, 11])
        self.land_form_type[land_form.meadows] = fuzz.trimf(self.land_form_type.universe, [10, 11, 12])
        self.land_form_type[land_form.arable_land] = fuzz.trimf(self.land_form_type.universe, [11, 12, 13])
        self.land_form_type[land_form.marshes] = fuzz.trimf(self.land_form_type.universe, [12, 13, 14])

    def populate_slope(self):
        # Populate slope with membership functions.
        self.slope[slope_ctgr.marshes_and_lowlands] = fuzz.trimf(self.slope.universe, [0, 1.5, 3])
        self.slope[slope_ctgr.flats_and_plateaus] = fuzz.trimf(self.slope.universe, [1.5, 3, 5])
        self.slope[slope_ctgr.flats_and_plateaus_in_combination_with_hills] = fuzz.trimf(self.slope.universe, [3, 5, 7])
        self.slope[slope_ctgr.hills_with_gentle_slopes] = fuzz.trimf(self.slope.universe, [5, 7, 8])
        self.slope[slope_ctgr.steeper_hills_and_foothills] = fuzz.trimf(self.slope.universe, [7, 12, 23])
        self.slope[slope_ctgr.hills_and_outcrops_of_mountain_ranges] = fuzz.trimf(self.slope.universe, [8, 23, 37])
        self.slope[slope_ctgr.higher_hills] = fuzz.trimf(self.slope.universe, [10, 37, 65])
        self.slope[slope_ctgr.mountains] = fuzz.trimf(self.slope.universe, [30, 65, 100])
        self.slope[slope_ctgr.highest_mountains] = fuzz.trimf(self.slope.universe, [50, 100, 100])

    def populate_imprevious(self):
        # Populate slope with membership functions.
        self.impervious[impervious_ctgr.marshes_and_lowlands] = fuzz.trimf(self.impervious.universe, [50, 100, 100])
        self.impervious[impervious_ctgr.flats_and_plateaus] = fuzz.trimf(self.impervious.universe, [30, 65, 100])
        self.impervious[impervious_ctgr.flats_and_plateaus_in_combination_with_hills] = fuzz.trimf(self.impervious.universe, [25, 30, 35])
        self.impervious[impervious_ctgr.hills_with_gentle_slopes] = fuzz.trimf(self.impervious.universe, [20, 25, 30])
        self.impervious[impervious_ctgr.steeper_hills_and_foothills] = fuzz.trimf(self.impervious.universe, [15, 20, 25])
        self.impervious[impervious_ctgr.hills_and_outcrops_of_mountain_ranges] = fuzz.trimf(self.impervious.universe, [10, 15, 20])
        self.impervious[impervious_ctgr.higher_hills] = fuzz.trimf(self.impervious.universe, [5, 10, 15])
        self.impervious[impervious_ctgr.mountains] = fuzz.trimf(self.impervious.universe, [0, 5, 10])
        self.impervious[impervious_ctgr.highest_mountains] = fuzz.trimf(self.impervious.universe, [0, 0, 5])


membership = Memberships()