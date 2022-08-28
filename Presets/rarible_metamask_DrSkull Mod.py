
# Edited by @Daemonrat :)

###ATTENTION####   This Code is Only works with MetaMask and RARIB collections on the Rarible (ethereum-single)  ###ATTENTION###

#make sure to set your variables below for this script, examples provided

#####VARIABLE START####### (FILL BEFORE STARTING) ####


start_num = 420 #the number of the first file to start from (files must be aranged numerically)
listing_option= 'Fixed price' ### 'Timed auction' ### 'Fixed price' ###change 'Open for bids' as desired## 		
loop_price = 0.069    		 #Please Enter Your Price here
loop_title = "Amazing Bananas! #"  	 #Please Enter Your Title name here
loop_file_format = "png" 	 #Please provide your format "png" , "jpg" , "mp4"
loop_description = "The Amazing Banana Collection features a variety of Amazing Banana NFTs that are sure to be Amazing! From traditional concepts to more abstract takes on the classic banana, there's something for everyone in this fun and whimsical collection. "  #please enter your description here
minimum_bid = 0.005 #Your Minimum Bind if your listing option is 'open for bids!'
expiration_date = "12.25.2022 11:59 PM" #Please Enter Your Expiration Date here if you have choosen 'Fixed Price'.
royalties = "10"
#facebook_hashtags = "This is an #Automated Post. Hello World Nice to See You. #Testing #coder"
#twitter_hashtags = "This is an #Automated Post. Hello World Nice to See You. #Testing #coder"
#####VARIABLES END########


from tkinter import EXCEPTION
from colorama import Fore,Back,Style 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver.set_window_size(360, 840)
while loop_amount != 0:
	print("Uploading: " + str(start_num) + "  -  " + str(loop_amount) + " to go...")
	driver.switch_to.window(driver.window_handles[0])
	print("window names " , driver.window_handles)
	go_to("https://rarible.com/create/start/ethereum")
	css_and_click("button[id='create-single']")
	while True:
		try:
			print("Checking for draft discard button, please wait...")
			x = wait.until(ExpectedConditions.presence_of_element_located((By.CSS_SELECTOR, "button[data-marker='restore-modal/discardButton']")))
			x.click()
			break
		except Exception as wtf:
			break

	if opsys == "Darwin":
		imagePath = os.path.abspath(file_folder + "/" + str(start_num) + "." + loop_file_format)
	else:
		imagePath = os.path.abspath(file_folder + "\\" + str(start_num) + "." + loop_file_format)

	css_and_key("input[name='primary-attachment']", imagePath)
	time.sleep(1)
	css_and_click("img[alt='{list_op}']".format(list_op = listing_option)) 
	time.sleep(1)

	if listing_option == "Fixed price":
		css_and_key("input[data-marker='root/appPage/create/form/price/input/priceInput']", loop_price)
	elif listing_option == "Timed auction":
		xpath_and_key('/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[4]/div/div[2]/div[1]/input', minimum_bid, "minimum bid full xpath not found")
		print("minimum bid entered Sucessfully")
		xpath_and_click('//*[@id="root"]/div[2]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[5]/div/div/div[2]/div/div[2]/div[2]/button',  "Drop Down arrow short xpath not found")
		xpath_and_click('/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[5]/div/div/div[3]/div/div/div/div/div[1]/div/div/button[5]',  "Pick Specific Date full xpath not found")
		xpath_and_click('//*[@id="root"]/div[2]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[5]/div/div/div[2]/div/div[2]/div/div[1]/button',  "close Button short xpath not found")
		print("this line is left intentionally")
		end_date= wait.until(ExpectedConditions.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[5]/div/div/div[2]/div/div[3]/div/div[1]/div/div/input')))
		end_date.send_keys(Keys.CONTROL + "a"); 
		end_date.send_keys(Keys.BACKSPACE); 
		end_date.send_keys(expiration_date); 
		
		
		print("Timed Auction Details Entered Successfully!")
	elif listing_option == "Open for bids":
		pass
	else:
		print("please pick listing option")
		time.sleep(1)

	time.sleep(1)
	css_and_key("input[data-marker='root/appPage/create/form/nameInput']", loop_title+str(start_num))
	time.sleep(3)
	css_and_key("textarea[testid='root/appPage/create/form/descriptionInput']", loop_description)
	
	x = wait.until(ExpectedConditions.presence_of_element_located((By.CSS_SELECTOR, "input[data-marker='root/appPage/create/form/royaltiesInput']")))
	x.send_keys(Keys.BACKSPACE)
	x.send_keys(Keys.BACKSPACE)
	x.send_keys(royalties)
	
	main_page = driver.current_window_handle
	css_and_click("button[data-marker='root/appPage/create/form/createButton']")

	
	time.sleep(5)
	while True:
		while True:
			try:
				
				t= driver.find_element_by_xpath("//button[normalize-space()='Try again']")
				driver.execute_script("arguments[0].click();", t)   
				print(Fore.RED,"Try again 1 found and clicked")
				Fore.WHITE
				
			except Exception as wtf:
				print("try again 1 not found. skipping")
				break
		try:
			print("Waiting for metamask popup, please wait...")
			time.sleep(5)
			for handle in driver.window_handles:
				if handle != main_page:
					login_page = handle
			driver.switch_to.window(login_page)
			break
		except Exception as wtf:
			print("Metamask popup not found.there might be a 'second try again', retrying...")
			try:
				print("checking if there is a second try")
				tr= driver.find_element_by_xpath("//button[normalize-space()='Try again']")
				driver.execute_script("arguments[0].click();", tr)   
				print(Fore.RED,"Try again 2 found and clicked")
				Fore.WHITE
			except Exception as wtf:
				print(Fore.WHITE,"try again 2 not found. skipping")
	try:
		xpath_and_click('//*[@id="app-content"]/div/div[2]/div/div[3]/div[1]')    
		print("scrolled down and clicked")
		time.sleep(5)
	except Exception as wtf:
		pass
		break
			
	css_and_click("button[class='button btn--rounded btn-primary']")
	time.sleep(1)
	driver.switch_to.window(main_page)

	if listing_option == "Fixed price":
		while True:
			while True:
				try:
					
					t= driver.find_element_by_xpath("//button[normalize-space()='Try again']")
					driver.execute_script("arguments[0].click();", t)   
					print(Fore.RED,"Try again 1 found and clicked")
					Fore.WHITE
					
				except Exception as wtf:
					print("try again 1 not found. skipping")
					break
			
			
			try:
				print("Waiting for metamask popup(fixed price0), please wait...")
				time.sleep(5)
				for handle in driver.window_handles:
					if handle != main_page:
						login_page = handle
				driver.switch_to.window(login_page)
				break
			except Exception as wtf:
				print("Metamask popup not found(fixed price 1), retrying...")
		xpath_and_click('//*[@id="app-content"]/div/div[2]/div/div[3]/div[1]')    
		print("scrolled down and clicked")
		css_and_click("button[class='button btn--rounded btn-primary']", "waiting for second sign window...")
		time.sleep(1)
	else:  
		while True:
			try:
				print("Waiting for metamask popup(for second sign), please wait...")
				time.sleep(5)
				for handle in driver.window_handles:
					if handle != main_page:
						login_page = handle
				driver.switch_to.window(login_page)
				break
			except Exception as wtf:
				print("Metamask popup not found(there might be a third try), retrying...")
				try:
					print("checking if there is a third try")
					tr3= driver.find_element_by_xpath("//button[normalize-space()='Try again']")
					driver.execute_script("arguments[0].click();", tr3)   
					print(Fore.RED,"Try again 3 found and clicked")
					Fore.WHITE
				except Exception as wtf:
					print("try again 3 not found. skipping")
		try:
			driver.switch_to.window(login_page)
			sc=driver.find_element_by_xpath('//*[@id="app-content"]/div/div[2]/div/div[3]/div[1]')    
			driver.execute_script("arguments[0].click();", sc)  
			print("scrolled down and clicked")
			xpath_and_click("//*[@id='app-content']/div/div[2]/div/div[3]/button[2]", "waiting for second sign window...")
		except Exception as wtf:
			print("second scroll not found. skipping")
			driver.switch_to.window(login_page)
			xpath_and_click("//*[@id='app-content']/div/div[2]/div/div[3]/button[2]", "waiting for second sign window...")
			
		time.sleep(1)
	driver.switch_to.window(main_page)
	#xpath_and_click("//*[@id='root']/div[1]/div/div/div/div/div/div/div[3]/div/div[2]/div/div/div[1]/div/button" ,"sharing not working...")
	#while True:
		#try:
			#print("Waiting for Tweet Window popup, please wait...")
			#time.sleep(5)
			#for handle in driver.window_handles:
				#if handle != main_page:
					#twitter_page = handle
					
			#driver.switch_to.window(twitter_page)
			#print("handle is selected, "+ driver.title)
			
		##except Exception as wtf:
			#print("Tweet button not found, retrying...")
		#try:
			#wait_for_xpath("//div[@class='r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-1ttztb7']//div[@aria-label='Tweet text']")
			#textbox = driver.find_element_by_xpath("//div[@class='r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-1ttztb7']//div[@aria-label='Tweet text']") #regular 
			#print("TWITTER textbox found")
		#except:
			#wait_for_xpath("//div[@role='dialog']//div//div//div//div//div//div//div//div//div//div//div//div//div//div//div//div//div//div//div//div//div//label//div//div[@dir='auto']//div//div//div//div//div[@aria-label='Tweet text']")
			#textbox = driver.find_element_by_xpath("//div[@role='dialog']//div//div//div//div//div//div//div//div//div//div//div//div//div//div//div//div//div//div//div//div//div//label//div//div[@dir='auto']//div//div//div//div//div[@aria-label='Tweet text']")
			#print(Fore.MAGENTA+"textbox alternate2 found")
		
		#print("textbox  clicked")
		#textbox.send_keys(twitter_hashtags)
		#print("hashtags sent to textbox")
		#time.sleep(1)
		#break
	#time.sleep(1)
	#xpath_and_click("/html/body/div[1]/div/div/div[2]/main/div/div/div[2]/div/div/div/div/div[3]/div/div" ,"Tweet Button middle not Working...")  
	#print("Tweet button press successful...")					   	
	#driver.close() 
	#print("Tweet Window Successfully Closed")
	#driver.switch_to.window(main_page)
	#xpath_and_click('//*[@id="root"]/div[1]/div/div/div/div/div/div/div[3]/div/div[2]/div/div/div[2]/div/button',"facebook short xpath button not working.")
	#print("Button Found and clicked Successfully")
	#while True:
		#try:
			#print("Waiting for Facebook Window popup, please wait...")
			#time.sleep(5)
			#for handle in driver.window_handles:
				#if handle != main_page:
					#facebook_page = handle
					
			#driver.switch_to.window(facebook_page)
			#print("handle is selected, "+ driver.title)
			#break
		#except Exception as wtf:
			#print("Facebook window page not found, retrying...")
	#xpath_and_click("//textarea[@placeholder='Say something about this...']", "Typing in textbox not found...")
	#print("Typing in textbox found and clicked successfully")
	#xpath_and_key("//textarea[@placeholder='Say something about this...']", facebook_hashtags, "facebook hashtag xpath not found")
	#print("facebook hashtags entered successfully as per user defined")
	#xpath_and_click("//span[normalize-space()='Post to Facebook']", "Post to facebook  xpath not working")
	#print("post to facebook successful")
	driver.close 
	time.sleep(3)
	driver.switch_to.window(main_page)   
	start_num = start_num + 1
	loop_amount = loop_amount - 1







































