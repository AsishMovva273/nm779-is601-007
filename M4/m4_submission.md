<table><tr><td> <em>Assignment: </em> M4-Simple-Calc</td></tr>
<tr><td> <em>Student: </em> Naga Veda Manikanta Sai Asish Movva (nm779)</td></tr>
<tr><td> <em>Generated: </em> 10/16/2023 11:40:33 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/m4-simple-calc/grade/nm779" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <p>Make sure you're working in an up to date branch</p><ul><li><code>git checkout dev</code></li><li><code>git pull origin dev</code></li><li><code>git checkout -b M4-Simple-Calc</code></li></ul><p>This will likely be started in class.</p><p>Steps:</p><ol><li>Create a new Folder called M4</li><li>Create a new file called MyCalc.py inside this folder</li><li>Create a MyCalc Class</li><li>Define basic addition / subtraction / multiplication / division functions<ol><li>These functions should update an internal variable as a running total/value called&nbsp;<code><b>ans</b></code></li><li>All functions must properly handle the math given standard math scenarios (i.e., show proper messages when trying to divide by zero for example)</li><li>Since you'll likely be taking screenshots of the code, make sure you add a comment with your ucid and the date</li></ol></li><li>Define a "main" logic to run when the program runs</li><li>This logic should ask for user input<ol><li>The input can be any valid number, any valid math operator, and any valid number (i.e., 2 * 2)<ol><li>This will do an immediate calculation, print it, and store the answer in the&nbsp;<code>ans</code>&nbsp;variable</li></ol></li><li>Alternatively, the input can be&nbsp;<code>ans</code>, any valid math operator, any valid number (i.e.,&nbsp;<code>ans</code>&nbsp;* 2)<ol><li>This will use the previous answer (or 0 if not set) as part of the calculation, print it, and will store the new answer in the&nbsp;<code>ans</code>&nbsp;variable</li></ol></li></ol></li><li>Create a test case for each scenario that utilize functions to have expected input and compare against expected output, all cases should pass (test cases should have a series of data passed into them)<ol><li>Test number-add-number</li><li>Test ans-add-number</li><li>Test number-sub-number</li><li>Test ans-sub-number</li><li>Test number-mult-number</li><li>Test ans-mult-number</li><li>Test number-div-number</li><li>Test ans-div-number</li></ol></li><li>Create a new file called m4_submission.md inside the M4 folder</li><li>Fill out the below deliverables</li><li>Generate the markdown and paste it into the m4_submission.md</li><li><code>git add .</code></li><li><code>git commit -m "adding m4 hw"</code></li><li><code>git push origin M4-Simple-Calc</code></li><li>Create a pull request M4-Simple-Calc to dev</li><li>Create a pull request dev to prod (after the previous one is merged)</li><li>Navigate to the prod branch on github, go to the M4 folder, click the m4_submission.md</li><li>Submit this link to Canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Code Snippets (Make sure each screenshot has a comment showing your ucid and the date it was written) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of valid Addition Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fnm779%2F2023-10-17T03.14.56image.png.webp?alt=media&token=a638f3e5-3c05-4d9c-927d-82a2047f668a"/></td></tr>
<tr><td> <em>Caption:</em> <p>this function adds the equation<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshot of valid Subtraction Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fnm779%2F2023-10-17T03.16.44image.png.webp?alt=media&token=78702f0d-c549-4d4e-bee9-7a4b353cc482"/></td></tr>
<tr><td> <em>Caption:</em> <p>This function subtracts the equation <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of valid Multiplication Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fnm779%2F2023-10-17T03.17.38image.png.webp?alt=media&token=85617551-1118-4f1c-8a50-41ad5fcb0ed8"/></td></tr>
<tr><td> <em>Caption:</em> <p>This function multiplies the equation <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshot of valid division Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fnm779%2F2023-10-13T00.09.23image.png.webp?alt=media&token=fa2df534-260d-429a-8974-a9d222f0be5b"/></td></tr>
<tr><td> <em>Caption:</em> <p>This function divides the equation.it prints error if the given equation is divided<br>by zero <br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fnm779%2F2023-10-17T03.19.12image.png.webp?alt=media&token=667e4a24-997f-48b3-9417-8419f599f5a0"/></td></tr>
<tr><td> <em>Caption:</em> <p>This function divides the equation.it prints error if the given equation is divided<br>by zero<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Test Case Validations </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of passing number-add-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fnm779%2F2023-10-17T03.22.21image.png.webp?alt=media&token=e36c2869-53b1-4a43-9d00-1fca54323d09"/></td></tr>
<tr><td> <em>Caption:</em> <p>This is series of test case for addition function which checks the correctness<br>of calculator<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of passing ans-add-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fnm779%2F2023-10-17T03.23.39image.png.webp?alt=media&token=1a30386f-0ded-4ed5-802a-ee81e77ed375"/></td></tr>
<tr><td> <em>Caption:</em> <p>This is series of test case for addition function which checks the correctness<br>of calculator<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of passing number-sub-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fnm779%2F2023-10-17T03.24.56image.png.webp?alt=media&token=87feb3ad-d82d-4a2e-9313-c91ff759982c"/></td></tr>
<tr><td> <em>Caption:</em> <p>This is series of test case for subtraction function which checks the correctness<br>of calculator<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshots of passing ans-sub-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fnm779%2F2023-10-17T03.25.45image.png.webp?alt=media&token=de151b6d-5b0f-4e31-94f8-0aaa78e1163a"/></td></tr>
<tr><td> <em>Caption:</em> <p>This is series of test case for subtraction function which checks the correctness<br>of calculator<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Screenshots of passing number-mult-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fnm779%2F2023-10-17T03.26.51image.png.webp?alt=media&token=81199d08-8561-4387-a3c0-8d93d76819f2"/></td></tr>
<tr><td> <em>Caption:</em> <p>This is series of test case for multiplication function which checks the correctness<br>of calculator<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Screenshots of passing ans-multi-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fnm779%2F2023-10-17T03.27.03image.png.webp?alt=media&token=62989996-d9e8-4390-a1bc-23ca5d617697"/></td></tr>
<tr><td> <em>Caption:</em> <p>This is series of test case for multiplication function which checks the correctness<br>of calculator<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 7: </em> Screenshots of passing number-div-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fnm779%2F2023-10-17T03.27.37image.png.webp?alt=media&token=1f40b41b-6c53-4a1d-8169-c02ce75d081c"/></td></tr>
<tr><td> <em>Caption:</em> <p>This is series of test case for divison function which checks the correctness<br>of calculator<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 8: </em> Screenshots of passing ans-div-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fnm779%2F2023-10-17T03.27.52image.png.webp?alt=media&token=985404bd-ba54-4235-90f0-c2ebffa5b690"/></td></tr>
<tr><td> <em>Caption:</em> <p>This is series of test case for divison function which checks the correctness<br>of calculator<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Briefly talk about anything you learn during this assignment/module</td></tr>
<tr><td> <em>Response:</em> <p>I&#39;ve learned some basic commands from linux and applying series of testcases<br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Discuss how test cases work and anything new you learned about them while doing this assignment, specially include how fixtures and parameterized tests work</td></tr>
<tr><td> <em>Response:</em> <p>This is simple calculator that can perform basic arithmetic operations (addition, subtraction, multiplication,<br>and division) based on user input. It maintains a running total (&#39;ans&#39;). The<br>user interacts with the calculator in a command-line interface, repeatedly inputting math expressions<br>until they choose to exit. The code also handles division by zero and<br>provides a &#39;quit&#39; option.&nbsp;The test case code&nbsp; contains a series of test functions<br>for a <code>MyCalc</code> class. These tests validate arithmetic operations like addition, subtraction, multiplication,<br>and division and the functionality of using &quot;ans&quot; as an operand in calculations.<br>Each test creates a <code>MyCalc</code> instance, performs calculations, and checks if the expected<br>results match the actual results using assertions. These tests ensures the correctness of<br>the calculator.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the pull request of M4-Simple-Calc to Dev link</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/AsishMovva273/nm779-is601-007/pull/3">https://github.com/AsishMovva273/nm779-is601-007/pull/3</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/m4-simple-calc/grade/nm779" target="_blank">Grading</a></td></tr></table>