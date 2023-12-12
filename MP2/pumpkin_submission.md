<table><tr><td> <em>Assignment: </em> IS601 - Mini Project 2 - Pumpkins</td></tr>
<tr><td> <em>Student: </em> Naga Veda Manikanta Sai Asish Movva (nm779)</td></tr>
<tr><td> <em>Generated: </em> 12/11/2023 6:54:54 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-mini-project-2-pumpkins/grade/nm779" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Create a new branch per the desired branch name below</li><li>Add the baseline files from the following link:&nbsp;<a href="https://gist.github.com/MattToegel/bb0d25257414c7154267baf0931dbef4">https://gist.github.com/MattToegel/bb0d25257414c7154267baf0931dbef4</a></li><li>Put them into a subfolder in your repository folder (I called my folder MP2)</li><li>Create a test folder as a subdirectory of MP2</li><li>git add .</li><li>git commit -m "baseline files"</li><li>git push origin (name of desired branch below)</li><li>You can go to github and open the pull request for evidence capturing later (don't close/merge the pull request until you're done with the assignment)</li><li>Do the below tasks and fill in the below entries</li><ol><li>git add/commit after any significant changes to build up history</li></ol><li>Save the below input and generate the submission markdown file (copy to clipboard or download the file)</li><li>Name it something relevant to the assignment if it's not named already</li><li>git add the submission file</li><li>git commit the submission file</li><li>git push the submission file</li><li>Complete the pull request to dev</li><li>Create a pull request from dev to prod</li><li>Go to the prod branch on github, navigate to the submission file</li><li>Paste that link to Canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Code Changes - Add the calculate_cost() implementation </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of the updated method calculate_cost()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fnm779%2F2023-12-07T23.26.19image.png.webp?alt=media&token=987542f3-6942-4b37-b710-4f7e55e85d8a"/></td></tr>
<tr><td> <em>Caption:</em> <p>method for total cost calculation of pumpkins<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fnm779%2F2023-12-11T22.54.51image.png.webp?alt=media&token=9aed5f13-2686-4d6e-91fe-e127c73f918f"/></td></tr>
<tr><td> <em>Caption:</em> <p>currency format<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain the approach to implementing the calculation</td></tr>
<tr><td> <em>Response:</em> <div>This technique aids in determining the price of the goods included in the<br>inprogress_pumpkin array.&nbsp;</div><div>For handling currency format, one can use float formatting such as {.:2f}.<br>This shows the numbers to two decimal places in float format.</div><div><br></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Exception Handling </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of adjusted code to handle exceptions</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fnm779%2F2023-12-11T23.02.13image.png.webp?alt=media&token=bdc120ed-0e5d-4514-9452-4927ca38c55a"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code for OutOfStock, NeedsCleaning, InvalidChoice exceptions<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fnm779%2F2023-12-11T23.03.50image.png.webp?alt=media&token=762af9ef-d776-489f-90d5-2dea0e75370f"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code for ExceededReainingChoice, InvalidPayment exception<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fnm779%2F2023-12-11T23.04.28image.png.webp?alt=media&token=cbf220a6-8c2f-469b-8baa-b06331d68bbe"/></td></tr>
<tr><td> <em>Caption:</em> <p>Invalid and exceeding exception<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fnm779%2F2023-12-11T23.05.02image.png.webp?alt=media&token=a9943add-aada-489b-bd8c-cd1f01127075"/></td></tr>
<tr><td> <em>Caption:</em> <p>Machine clean exception<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Summarize each exception handling process</td></tr>
<tr><td> <em>Response:</em> <div>This is where OutOfStockException is handled, and the user is presented with a<br>message indicating that the item they are attempting to add is indeed out<br>of stock.</div><div>&nbsp; &nbsp; The array must always be cleaned once it is loaded<br>with merchandise in order to provide room for the items for the following<br>customers. This is handled by NeedsCleaningException, which publishes the message after cleaning. Cleaning<br>can be done by providing a "clean" keyword.</div><div>&nbsp; &nbsp; Every time a user<br>tries to enter an invalid item that isn't in the list of pumpkins,<br>an InvalidChoiceException is raised. Additionally, the category in which this issue occurred is<br>indicated in the notification.</div><div>&nbsp; &nbsp; When a user tries to add more products<br>than the maximum allowable range specified for each category, an ExceededRemainingChoicesException is raised,<br>and we force the user to follow selection for the next categories by<br>shifting the selection to the next category.</div><div>&nbsp; &nbsp; When a user attempts to<br>input an amount other than the total that is displayed, an appropriate message<br>prompting the user to provide the entire amount to complete payment is displayed,<br>raising an InvalidPaymentException.</div><div>&nbsp; &nbsp;&nbsp;</div><div><br></div><div><br></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Test Cases </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of test cases per the checklist</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fnm779%2F2023-12-11T23.13.17image.png.webp?alt=media&token=f8cf1fd6-6179-4f50-b1f4-116a5504d87e"/></td></tr>
<tr><td> <em>Caption:</em> <p>test_pumpkin_first_selection, test_add_face_stencils_if_in_stock,test_add_extras_if_in_stock<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fnm779%2F2023-12-11T23.14.08image.png.webp?alt=media&token=4d3edc63-e0ea-4fea-a5bb-faef475880d2"/></td></tr>
<tr><td> <em>Caption:</em> <p>test_add_up_to_3_face_stencils, test_add_up_to_3_extras<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fnm779%2F2023-12-11T23.15.58image.png.webp?alt=media&token=334fb584-b8a7-4cf7-851d-beb7cd2ebb16"/></td></tr>
<tr><td> <em>Caption:</em> <p>test_cost_calculation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fnm779%2F2023-12-11T23.16.52image.png.webp?alt=media&token=4d75ba5b-8332-4fd2-8c7c-cea5ff56a2fa"/></td></tr>
<tr><td> <em>Caption:</em> <p>test_total_sales_calculation, test_total_products_increment<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fnm779%2F2023-12-11T23.17.26image.png.webp?alt=media&token=8f93bd3d-e1b2-49e0-af1b-aededb10146d"/></td></tr>
<tr><td> <em>Caption:</em> <p>All test results<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Summarize each test case logic</td></tr>
<tr><td> <em>Response:</em> <div>Test 1: The pumpkin must be the initial choice; additional or face stencils<br>cannot be added without a pumpkin selection.We examine whether face stencils may be<br>applied without pumpkin in this example case.</div><div>Test 2: Face stencils can only be<br>added if they are available. In this test scenario, we examine whether adding<br>more stencils than what is advised will result in an exception being triggered.</div><div>Test<br>3: Extras can only be added if they are available.</div><div>&nbsp;In this test scenario,<br>we examine whether adding more than the suggested additional will result in the<br>raising of an exception.</div><div>Test 4: You can add any three face stencil combinations.&nbsp;</div><div>We<br>examine if three face stencils can be applied in any configuration in this<br>test instance.</div><div><div>Test 5: You can add three additionals in any arrangement.</div><div>&nbsp;We examine whether<br>adding three extras in any combination is possible in this test situation.</div><div>Test 6:<br>The cost needs to be accurately computed using the options; part of this<br>involves checking the currency format. (A few variants of at least three genuine<br>pumpkins should be included in the test case; hint: parameterized testing)&nbsp;</div><div>We verify the<br>accuracy of the overall calculation of all the goods in this test scenario.</div><div>Test<br>7: The amount of the expenses, or total sales, needs to be computed<br>correctly. The test case should include a few variations of at least three<br>legitimate pumpkins (hint: parameterized tests).</div><div>&nbsp;We verify that the Total Sales Value is computed<br>correctly in this test instance.</div></div><div><div>Test 8: With each transaction, the total products variable<br>should appropriately increase.</div><div>We examine whether or not the product upgrade was implemented correctly<br>in this test scenario.</div></div><div><br></div><div><br></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add pull request for the assignment</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/AsishMovva273/nm779-is601-007/pull/12">https://github.com/AsishMovva273/nm779-is601-007/pull/12</a> </td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain any issues/difficulties or something you learned while doing this assignment</td></tr>
<tr><td> <em>Response:</em> <p>lot of difficulties with the code and while creating virtual environment.I had to<br>change the python interpreter later fixed all the errors&nbsp;<br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of successful output</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fnm779%2F2023-12-11T23.25.25image.png.webp?alt=media&token=b04d887e-0688-4845-9fd5-a6d1c4c65b1c"/></td></tr>
<tr><td> <em>Caption:</em> <p>Execution of program for different testcases<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-mini-project-2-pumpkins/grade/nm779" target="_blank">Grading</a></td></tr></table>