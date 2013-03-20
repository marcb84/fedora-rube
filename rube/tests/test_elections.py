# This file is part of Rube.
#
# Rube is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Rube is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with Rube. If not, see <http://www.gnu.org/licenses/>.
#
# Authors:
#     Ralph Bean <rbean@redhat.com>
#     Remy DeCausemaker <remyd@civx.us>

import rube
import time

from selenium.webdriver.common.keys import Keys


class TestElections(rube.RubeTest):
    base = "https://admin.stg.fedoraproject.org/voting"
    title = "Fedora Elections"

    def test_login(self):
        self.driver.get(self.base)
        elem = self.driver.find_element_by_css_selector("input.button")
        elem.click()

        elem = self.driver.find_element_by_css_selector("#user_name")
        elem.send_keys(self.auth[0])
        elem = self.driver.find_element_by_css_selector("#password")
        elem.send_keys(self.auth[1])
        elem.send_keys(Keys.RETURN)

        time.sleep(2)
        self.wait_for("Welcome, %s" % self.auth[0])
