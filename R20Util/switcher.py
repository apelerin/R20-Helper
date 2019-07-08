import re
from selenium.webdriver.common.keys import Keys



def switcher(message, driver):
	chat_input = driver.find_element_by_xpath("/html/body/div[16]/textarea")
	command = message.split()[1]
	if re.search("^CoefCombat.*\)$", command) != None:
		coef_combat(command, chat_input)
		

def coef_combat(command, chat_input):
	grid = [[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 'RA', 'RA', 'RA', 'RA', 'RA', 'RA', 'RA', 'RA', 'RA', 'RA', 'RA', 'RA'],
			[1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 19, 'RA', 'RA', 'RA', 'RA', 'RA', 'RA', 'RA', 'RA', 'RA', 'RA', 'RA'],
			[1, 2, 3, 5, 7, 9, 11, 13, 15, 17, 18, 19, 'RA', 'RA', 'RA', 'RA', 'RA', 'RA', 'RA', 'RA', 'RA', 'RA'],
			['EA', 1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 18, 19, 'RA', 'RA', 'RA', 'RA', 'RA', 'RA', 'RA', 'RA', 'RA'],
			['EA', 1, 2, 4, 5, 7, 9, 11, 13, 15, 17, 18, 18, 19, 19, 'RA', 'RA', 'RA', 'RA', 'RA', 'RA', 'RA'],
			['EA', 'EA', 1, 3, 5, 6, 8, 10, 12, 14, 16, 17, 18, 18, 19, 19, 'RA', 'RA', 'RA', 'RA', 'RA', 'RA'],
			['EA', 'EA', 1, 3, 4, 6, 7, 9, 11, 13, 15, 17, 17, 18, 18, 19, 19, 'RA', 'RA', 'RA', 'RA', 'RA'],
			['EA', 'EA', 'EA', 2, 4, 5, 7, 8, 10, 12, 14, 16, 17, 17, 18, 18, 19, 19,'RA', 'RA', 'RA', 'RA'],
			['EA', 'EA', 'EA', 2, 3, 5, 7, 8, 9, 11, 13, 15, 15, 17, 17, 18, 18, 19, 19,'RA', 'RA', 'RA'],
			['EA', 'EA', 'EA', 1, 3, 4, 6, 8, 8, 10, 12, 14, 16, 16, 17, 17, 18, 18, 19, 19, 'RA', 'RA'],
			['EA', 'EA', 'EA', 1, 2, 4, 6, 7, 8, 9, 11, 13, 14, 15, 16, 16, 17, 17, 18, 18, 19, 'RA'],
			['EA', 'EA', 'EA', 'EA', 2, 3, 5, 7, 7, 9, 11, 11, 13, 14, 15, 15, 16, 16, 17, 17, 18, 18],
			['EA', 'EA', 'EA', 'EA', 1, 3, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 15, 16, 16, 17, 17, 18],
			['EA', 'EA', 'EA', 'EA', 1, 2, 4, 6, 6, 8, 10, 10, 12, 12, 13, 14, 14, 15, 15, 16, 16, 17, 17],
			['EA', 'EA', 'EA', 'EA', 'EA', 2, 4, 6, 6, 8, 10, 10, 12, 12, 13, 14, 14, 14, 15, 15, 16, 16, 17],
			['EA', 'EA', 'EA', 'EA', 'EA', 2, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 14, 15, 15, 16, 16, 17],
			['EA', 'EA', 'EA', 'EA', 'EA', 1, 3, 5, 5, 7, 9, 9, 10, 11, 13, 13, 14, 14, 14, 15, 15, 16, 16],
			['EA', 'EA', 'EA', 'EA', 'EA', 'EA', 2, 4, 4, 6, 8, 8, 9, 10, 11, 12, 14, 14, 15, 15, 16, 16],
			['EA', 'EA', 'EA', 'EA', 'EA', 'EA', 2, 3, 4, 5, 7, 7, 8, 9, 11, 11, 13, 14, 15, 15, 16, 16],
			['EA', 'EA', 'EA', 'EA', 'EA', 'EA', 1, 3, 3, 5, 6, 7, 7, 8, 10, 11, 12, 13, 15, 15, 16, 16],
			['EA', 'EA', 'EA', 'EA', 'EA', 'EA', 1, 2, 3, 4, 5, 6, 6, 7, 9, 10, 11, 12, 14, 15, 16, 17],
			['EA', 'EA', 'EA', 'EA', 'EA', 'EA', 'EA', 2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 16 ,17]]
	param = list(map(int, re.split('\(|\)', command)[1].split(',')))
	if isinstance(grid[param[0]][param[1] + param[2]], int):
		chat_input.send_keys("Valeur d'attaque: " + grid[param[0]][param[1] + param[2]])
	elif grid[param[0]][param[1] + param[2]] == "EA":
		chat_input.send_keys("Échec automatique")
	else:
		chat_input.send_keys("Réussite automatique")
	chat_input.send_keys(Keys.RETURN)