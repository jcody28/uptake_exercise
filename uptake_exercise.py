## Uptake Coding Exercise
##   by Jim Cody
##
## Used:
##   Python 2.7.6
##   Selenium 2.53.6
# Imports
import unittest
from selenium import webdriver

class UptakeExercise( unittest.TestCase ):
	def setUp( self ):
		# I'm a fan of both Firefox and Chrome, but only used Firefox for this Exercise
		self.driver = webdriver.Firefox()
		
	# I could have done multiple unittest tests, but chose to do this all in one since the 
	#  complexity level is not too high
	def test_uptake_exercise( self ):
		driver = self.driver
		driver.get( "http://uptake.com/" )
		# Validate the Title after opening the Uptake Homepage - pretty boring I know
		self.assertIn( "Home | Uptake", driver.title )
		
		# Find the top-right 'People' link and click it
		people_link = driver.find_element_by_id( 'menu-item-4162' )
		people_link.click()
		
		# Validate the Title after selecting the 'People' page-link
		self.assertIn( "People | Uptake", driver.title )
		
		# Scroll Down a bit to where the Panels can be selected
		driver.execute_script( "window.scrollTo( 0, 2050 )" )
		
		# Find 'Curiosity' panel button
		curiosity_selector = driver.find_element_by_xpath( "//a[@class='ghost-btn ghost-btn--value ghost-btn--grey'][@data-slide='curiosity']" )
		
		# Before we click the 'Curiosity' panel button - validate the content of the current active 'panel__features__body' element (Clarity)
		panel_content = driver.find_element_by_xpath( "//div[@class='panel__features__content']/div[@class='panel__features__content--clarity is-active']/div[@class='panel__features__body']" )
		self.assertIn( "We ask questions. All the time.", panel_content.get_attribute( 'innerHTML' ) )
		
		# Select the 'Curiosity' panel button
		curiosity_selector.click()
		
		# What is the content of the now active 'panel__features__body' element (should be Curiosity)
		panel_content = driver.find_element_by_xpath( "//div[@class='panel__features__content']/div[@class='panel__features__content--curiosity is-active']/div[@class='panel__features__body']" )
		self.assertIn( "We build amazing things by finding opportunities to learn together.", panel_content.get_attribute( 'innerHTML' ) )
		
		# Find 'Flexibility' panel button and select it
		flexibility_selector = driver.find_element_by_xpath( "//a[@class='ghost-btn ghost-btn--value ghost-btn--grey'][@data-slide='flexibility']" )
		flexibility_selector.click()
		
		# Validate content of the 'panel__features__body' after the above selection
		panel_content = driver.find_element_by_xpath( "//div[@class='panel__features__content']/div[@class='panel__features__content--flexibility is-active']/div[@class='panel__features__body']" )
		self.assertIn( "Thinking like entrepreneurs helps us to stay nimble and keep evolving.", panel_content.get_attribute( 'innerHTML' ) )
		
		# Scroll up to top of page
		driver.execute_script( "window.scrollTo( 0, 0 )" )
		
		# Find the Uptake Logo element and select it to get back to the Uptake Homepage
		uptake_home = driver.find_element_by_xpath( "//a[@class='l-site-header__logo']" )
		uptake_home.click()
		self.assertIn( "Home | Uptake", driver.title )
		
	def tearDown( self ):
		self.driver.close()

if __name__ == "__main__":
	unittest.main()
