<table><tr><td> <em>Assignment: </em> IS601 Mini Project 3 - Thankful Giving</td></tr>
<tr><td> <em>Student: </em> Naga Veda Manikanta Sai Asish Movva (nm779)</td></tr>
<tr><td> <em>Generated: </em> 12/13/2023 7:13:48 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-mini-project-3-thankful-giving/grade/nm779" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <p><b>Initial Prep:</b><div><ol><li>Create a new app on heroku called course-section-ucid-td</li><ol><li>replace course, section, ucid accordingly</li></ol><li>Go to the Settings tab of the app and add the config var of DB_URL and your DB connection string<br></li><li>Go to your github repository and go to Settings and add a new repository secret called&nbsp;HEROKU_APP_NAME_MP3 and fill in your new app name as the value</li><li>Note: we will just have one instance</li><li>Grab the yml file from the shared branch containing the initial code templates and put it in your .github/workflows folder, you shouldn&#39;t need to edit it</li><li>Make sure Wakatime is setup correctly and recording time correctly</li></ol><div>Baseline code:&nbsp;<a href="https://github.com/MattToegel/IS601/tree/F23-MiniProject-3">https://github.com/MattToegel/IS601/tree/F23-MiniProject-3</a>&nbsp;</div><div>Example Site:&nbsp;<a href="https://is601-mt85-td-f7d7f9bec981.herokuapp.com">https://is601-mt85-td-f7d7f9bec981.herokuapp.com</a></div><div><br></div><div><b>Primary Instructions:</b></div></div><div><ol><li>Checkout any latest branch (dev is fine) and pull the latest changes</li><li>Create a new branch per the recommended name below</li><li>Copy the rest of the files from the shared branch containing the initial code templates</li><ol><li>It&#39;s important that you have just one folder for this project at the root level of your repository, in my example I called mine MP3 and it contains the entire app</li><li>Make sure the .csv files are copied as csv data and not html tables (github may try to render them so choose the &quot;Raw&quot; button of the file to get the raw text)</li></ol><li>Create a virtual environment inside the MP3 related folder and pip install the requirements.txt (you shouldn&#39;t need to manually add anything else)</li><li>Copy your .env file from flask_sample into MP3 (again this should gray out as it should be in the .gitignore files) but it&#39;s necessary for local development</li><li>Once everything is copied over immediately add/commit the changes and record the commit message as something similar to &quot;template files&quot;</li><li>Push the baseline and open a pull request from this branch to dev (don&#39;t merge it until you have the markdown file)</li><li>Execute the init_db.py file for this project to generate the two required tables</li><li>Proceed to solve/implement the missing pieces noted by &quot;TODO&quot; comments throughout the code (which are also shown below in the various deliverables)</li><li>As soon as you start working on an item add your ucid-date as a comment so you don&#39;t forget</li><li><b>Add and commit after each TODO item (or relatively frequently to build up a proper history; do not save this process for the end)</b></li><li>For the below deliverables, you&#39;ll be capturing screenshots from your new heroku app (ensure the url is clearly visible)</li><li>Once finished, copy the markdown or download the file and add it to your MP3 related folder as a .md file (don&#39;t forget the extension)</li><li>Do your final add/commit/push once satisfied that everything is all set</li><li>Merge the pull request that was opened in step 7</li><ol><li>This will trigger a deploy to dev (due to the original yml files) but this app won&#39;t be affected</li></ol><li>Create a pull request from dev to prod and merge it</li><ol><li>This will trigger a deploy to prod (due to the original yml files) but this app won&#39;t be affected</li></ol><li>From the prod branch on github, navigate to your submission.md file and grab that link to paste to Canvas</li></ol><div><b>Objective/Project Description:</b></div></div><div>You&#39;ll be implementing a cross-organization Thanksgiving Drive application.</div><div>There will be CRUD operations to manage organizations and CRUD operations to manage donations related to organizations as well as an import page to preload given data.</div><div>Some files are provided as fully working and should not be modified, typically they&#39;ll have comments like &quot;DO NOT EDIT&quot;.</div><div>Other files are basic skeleton files with a number of &quot;TODO&#39;s&quot; that you need to solve. It&#39;s best to make the code changes near where the particular TODO is (do not delete the TODO comments).</div><div>There are also provided test case files.</div><div>Between the TODOs and the tests you must implement the missing pieces to get all tests to pass for full credit.</div><div>Do not edit any of the test cases except for a caveat I&#39;ll mention in another paragraph below.</div><div><br></div><div><b>Caveat:</b><br>If you can&#39;t solve a test case first ensure you run <code>pytest -rA</code> locally to show and capture the test pass/fail summary, then for any of the cases you can&#39;t achieve add the word &quot;off_&quot; in front of the function name. (i.e., if a test is test_myfile() rename it to off_test_myfile()).</div><div>This will disable the test case allowing you to deploy to potentially receive partial credit.</div><div><br></div><div>Files you shouldn&#39;t edit:</div><div>layout.html</div><div>country_state_selector.html</div><div>flash.html</div><div>organization_dropdown.html</div><div>sort_filter.html</div><div>any test files (unless it&#39;s for the caveat)</div><div>requirements.txt</div><div>Dockerfile</div><div>any files in the sql folder</div><div>geography.py</div><div>index.py</div><div>main.py</div><div><br></div><div><br></div><div><br></div><div><br></div><div><br></div><div><br></div></p>
</td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Solving the index.html template </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the index.html page being shown and of the code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fnm779%2F2023-12-13T04.27.09image.png.webp?alt=media&token=31b241de-600c-44fc-af3d-d601a5260de8"/></td></tr>
<tr><td> <em>Caption:</em> <p>index.html<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fnm779%2F2023-12-14T00.10.14image.png.webp?alt=media&token=b6f14f83-967e-40d4-ad0a-10fb0329d0c1"/></td></tr>
<tr><td> <em>Caption:</em> <p>index page<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Solving the nav.html template </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots showing the navbar and the edited code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fnm779%2F2023-12-13T23.16.22image.png.webp?alt=media&token=bbc71ca5-05e4-4625-a89a-007f7108fb03"/></td></tr>
<tr><td> <em>Caption:</em> <p>Navbar html code<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Solving the admin upload </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots showing the code changes related to the checklist</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fnm779%2F2023-12-13T23.17.09image.png.webp?alt=media&token=a9e87608-c197-449f-a998-8dc5984a73c7"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code for import csv admin.py <br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fnm779%2F2023-12-13T23.17.39image.png.webp?alt=media&token=be038e28-c22b-47c8-94a1-f47db4bac1ec"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code for import csv admin.py <br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fnm779%2F2023-12-13T23.18.22image.png.webp?alt=media&token=7a245ef8-a3a3-4f1b-8d1b-bda7dace2d54"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code for import csv admin.py <br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Solve the donation related logic and requirements </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of create and edit views of donations (from the browser) and of the code of the html page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fnm779%2F2023-12-14T00.07.35image.png.webp?alt=media&token=f93610c8-1d4d-434d-8f89-5764ca126e6c"/></td></tr>
<tr><td> <em>Caption:</em> <p>Create donations<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fnm779%2F2023-12-14T00.08.00image.png.webp?alt=media&token=b49f022d-ca07-4d18-b490-409b5531e3d6"/></td></tr>
<tr><td> <em>Caption:</em> <p>Edit donations<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fnm779%2F2023-12-13T23.21.42image.png.webp?alt=media&token=f30bc798-0d3a-4ac7-a92c-95aae9a247ee"/></td></tr>
<tr><td> <em>Caption:</em> <p>Add donations code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fnm779%2F2023-12-13T23.21.59image.png.webp?alt=media&token=2760863e-68eb-4337-a754-ed7fca2c54a9"/></td></tr>
<tr><td> <em>Caption:</em> <p>Add donations code<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshots of the search page of donations (from the browser) and of the code of the html page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fnm779%2F2023-12-14T00.08.44image.png.webp?alt=media&token=214bc22e-2bdb-406f-9eef-361c6a4b8c8e"/></td></tr>
<tr><td> <em>Caption:</em> <p>Donations Search with no filters<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fnm779%2F2023-12-14T00.09.05image.png.webp?alt=media&token=2047f7db-c6dd-4062-85e1-fab019b72c3d"/></td></tr>
<tr><td> <em>Caption:</em> <p>Donations Search with filters<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fnm779%2F2023-12-13T23.23.53image.png.webp?alt=media&token=deee2438-5f46-4fd0-a083-8f869d43a240"/></td></tr>
<tr><td> <em>Caption:</em> <p>HTML search donations code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fnm779%2F2023-12-13T23.24.47image.png.webp?alt=media&token=cbe5d3db-7dce-44b1-af46-71295f8dc6d8"/></td></tr>
<tr><td> <em>Caption:</em> <p>HTML search donations code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fnm779%2F2023-12-13T23.25.08image.png.webp?alt=media&token=1300c839-4293-48d1-a591-f2f2486f81bc"/></td></tr>
<tr><td> <em>Caption:</em> <p>HTML search donations code<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add screenshots of the donations search route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fnm779%2F2023-12-13T23.29.55image.png.webp?alt=media&token=335ae030-9dd3-47ae-bdec-5c270b6d9bf7"/></td></tr>
<tr><td> <em>Caption:</em> <p>Donations Search route code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fnm779%2F2023-12-13T23.30.23image.png.webp?alt=media&token=5759c16c-1c5a-42e8-b67f-115308d5849a"/></td></tr>
<tr><td> <em>Caption:</em> <p>Donations Search route code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fnm779%2F2023-12-13T23.31.16image.png.webp?alt=media&token=ff0f4dd4-4781-4fc4-9110-9ed1873b5ee1"/></td></tr>
<tr><td> <em>Caption:</em> <p>Donations Search route code<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add screenshots of the donations add route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fnm779%2F2023-12-13T23.33.57image.png.webp?alt=media&token=3ea6cca3-30b0-483e-8899-bd9298be4264"/></td></tr>
<tr><td> <em>Caption:</em> <p>Donations add route code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fnm779%2F2023-12-13T23.34.39image.png.webp?alt=media&token=a7bdca90-1f66-43d8-96ed-66f560500347"/></td></tr>
<tr><td> <em>Caption:</em> <p>Donations add route code<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add screenshots of donations edit route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fnm779%2F2023-12-13T23.38.04image.png.webp?alt=media&token=e3d6f727-ce07-4fa3-b8bb-1fd3145f5f44"/></td></tr>
<tr><td> <em>Caption:</em> <p>Edit donations code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fnm779%2F2023-12-13T23.38.38image.png.webp?alt=media&token=8200af35-9580-4d2e-a6b8-3437b82de61c"/></td></tr>
<tr><td> <em>Caption:</em> <p>Edit donations code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fnm779%2F2023-12-13T23.38.55image.png.webp?alt=media&token=81c9cd62-ab53-4fcd-8f85-d2f0fc79ee38"/></td></tr>
<tr><td> <em>Caption:</em> <p>Edit donations code<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add screenshots of the donation delete route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fnm779%2F2023-12-13T23.39.17image.png.webp?alt=media&token=ef647a4f-b1a3-4955-83a0-656e20f0cb5b"/></td></tr>
<tr><td> <em>Caption:</em> <p>Delete donations code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fnm779%2F2023-12-14T00.06.19image.png.webp?alt=media&token=17270d3a-0c5e-41d5-a65d-4ae78e9d46d6"/></td></tr>
<tr><td> <em>Caption:</em> <p>successful delete<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Solve the organization related logic and requirements </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of create and edit views of organizations (from the browser) and of the html code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fnm779%2F2023-12-14T00.03.13image.png.webp?alt=media&token=8bb4d4a1-532d-4ef4-acdd-0fad459fd6ce"/></td></tr>
<tr><td> <em>Caption:</em> <p>Create organization<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fnm779%2F2023-12-14T00.03.43image.png.webp?alt=media&token=c824daf0-86e0-431f-91cc-8640280f9899"/></td></tr>
<tr><td> <em>Caption:</em> <p>Edit organization<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fnm779%2F2023-12-13T23.41.18image.png.webp?alt=media&token=5943a48f-fb98-40aa-9327-f4b5d0fb352e"/></td></tr>
<tr><td> <em>Caption:</em> <p>List organization<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fnm779%2F2023-12-13T23.42.09image.png.webp?alt=media&token=7033b0cf-7330-4d95-a435-ac37fa4a21b6"/></td></tr>
<tr><td> <em>Caption:</em> <p>List organizations html code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fnm779%2F2023-12-13T23.42.35image.png.webp?alt=media&token=db9bef43-59b9-489f-8ae8-cbbdecb129fc"/></td></tr>
<tr><td> <em>Caption:</em> <p>List organizations html code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fnm779%2F2023-12-13T23.43.47image.png.webp?alt=media&token=9378cf86-3a31-4055-a46f-eedd24773a2b"/></td></tr>
<tr><td> <em>Caption:</em> <p>Manage organization<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fnm779%2F2023-12-13T23.44.09image.png.webp?alt=media&token=2a429872-b243-416a-ad7b-b523d8aeffd5"/></td></tr>
<tr><td> <em>Caption:</em> <p>Manage organization<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshots of the search page of organizations (from the browser) and of the html code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fnm779%2F2023-12-14T00.04.15image.png.webp?alt=media&token=d5403cf8-ff8f-47a2-8343-1da29b249e79"/></td></tr>
<tr><td> <em>Caption:</em> <p>Search page of organization<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fnm779%2F2023-12-13T23.45.13image.png.webp?alt=media&token=9555e15e-a32f-4a47-9cc8-79b855aebbff"/></td></tr>
<tr><td> <em>Caption:</em> <p>organization Search html code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fnm779%2F2023-12-13T23.45.34image.png.webp?alt=media&token=0c1d37a2-7cab-4655-99ce-f96959ad3e93"/></td></tr>
<tr><td> <em>Caption:</em> <p>Organization search html code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fnm779%2F2023-12-13T23.45.53image.png.webp?alt=media&token=b870a8d5-330d-4295-919a-c51fc2289d4a"/></td></tr>
<tr><td> <em>Caption:</em> <p>Organization search html code<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the organization search route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fnm779%2F2023-12-13T23.47.30image.png.webp?alt=media&token=5d2a2ff9-ffc1-413e-aa8a-aea3888540ea"/></td></tr>
<tr><td> <em>Caption:</em> <p>Search organization route code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fnm779%2F2023-12-13T23.47.51image.png.webp?alt=media&token=7a719550-65cf-4ccb-8920-759aa5992560"/></td></tr>
<tr><td> <em>Caption:</em> <p>Search organization route code<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add screenshots of organization add route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fnm779%2F2023-12-13T23.49.40image.png.webp?alt=media&token=b2008b87-aa7c-41c8-8132-9f3080b5657e"/></td></tr>
<tr><td> <em>Caption:</em> <p>Add organization route code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fnm779%2F2023-12-13T23.50.01image.png.webp?alt=media&token=92b332c7-b02b-4698-84b7-e4eb30e4dea3"/></td></tr>
<tr><td> <em>Caption:</em> <p>Add organization route code<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add screenshots of organization edit route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fnm779%2F2023-12-13T23.50.23image.png.webp?alt=media&token=fd6da232-0ffb-4c2a-a023-ad0433d4b267"/></td></tr>
<tr><td> <em>Caption:</em> <p>Edit organization route code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fnm779%2F2023-12-13T23.50.47image.png.webp?alt=media&token=72446112-715f-4f00-80a5-1f0f9f189624"/></td></tr>
<tr><td> <em>Caption:</em> <p>Edit organization route code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fnm779%2F2023-12-13T23.51.26image.png.webp?alt=media&token=e28dfd93-aa05-4a3a-9a38-20c7382322e8"/></td></tr>
<tr><td> <em>Caption:</em> <p>Edit organization route code<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add screenshots of organization delete route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fnm779%2F2023-12-13T23.51.51image.png.webp?alt=media&token=f1373b69-6ea2-46f6-9f1f-34cd62c75656"/></td></tr>
<tr><td> <em>Caption:</em> <p>Delete organization route code<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Test cases </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of passing test_donations.py using -rA</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fnm779%2F2023-12-13T23.55.54image.png.webp?alt=media&token=e579295c-7e71-4b45-bbca-171c967a0b2b"/></td></tr>
<tr><td> <em>Caption:</em> <p>passing test_donations.py using -rA<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot of passing test_organizations.py using -rA</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fnm779%2F2023-12-13T23.56.34image.png.webp?alt=media&token=b536d20f-8011-46cc-86b9-dc619f736d48"/></td></tr>
<tr><td> <em>Caption:</em> <p> passing test_organizations.py using -rA<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add screenshot of passing test_upload.py using -rA</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fnm779%2F2023-12-13T23.57.21image.png.webp?alt=media&token=13e7c3d2-3845-4f08-8794-b062c23244c6"/></td></tr>
<tr><td> <em>Caption:</em> <p>passing test_upload.py using -rA<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add screenshot of passing test_index.py using -rA</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fnm779%2F2023-12-13T23.58.12image.png.webp?alt=media&token=bf0b8f5d-0a37-46cc-974a-4591d609ac0a"/></td></tr>
<tr><td> <em>Caption:</em> <p>passing test_index.py using -rA<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Did all tests pass? If no, list which failed and explain why</td></tr>
<tr><td> <em>Response:</em> <p>A few tests failed in test/test_donations.py::test_donation_list due to some data issues from the<br>test csv.<br><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add pull request link for this assignment branch</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/AsishMovv/IS601-007/pull/13">https://github.com/AsishMovv/IS601-007/pull/13</a> </td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshots of your commit history</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fnm779%2F2023-12-13T23.59.40image.png.webp?alt=media&token=952fa50b-7ad8-45a6-b83f-c756c884bcd6"/></td></tr>
<tr><td> <em>Caption:</em> <p>co<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of your wakatime dashboard for this class/project</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fnm779%2F2023-12-14T00.00.28image.png.webp?alt=media&token=84fb1a92-e561-44bb-aa2a-2c8576297228"/></td></tr>
<tr><td> <em>Caption:</em> <p>wakatime screenshot<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fnm779%2F2023-12-14T00.01.17image.png.webp?alt=media&token=5b46e9ee-6e51-4e14-ad0c-346b77c10af9"/></td></tr>
<tr><td> <em>Caption:</em> <p>wakatime screenshot<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a link to the application from the new vm/app</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-007-nm779-td-982924248aad.herokuapp.com/">https://is601-007-nm779-td-982924248aad.herokuapp.com/</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-mini-project-3-thankful-giving/grade/nm779" target="_blank">Grading</a></td></tr></table>