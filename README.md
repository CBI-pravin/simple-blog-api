# simple-blog-api

Thia is the simple blog website with CRUDE operations
1 > To register user type http://127.0.0.1:8000/api/register/ in url with POST method only 
    I had implemented token based authentication for user so we need to create new token while registering new user
    
    format of input to register new user : 
    
        {"name":"pravin",
        "email":"pravin@1234gmail.com",
        "password" :"Pravin@1234"
        }
        
     this will produce token  output like this :
     
        {
        "status": "success",
        "details": "account created successfully",
        "token": "f0b26fa7d47820c968ed30608d58d6a793e3ec95"
        }

2 > To login user type  http://127.0.0.1:8000/api/login/ with POST method only
      format of input to login user : 
         here username is the user's email address
      
        {"username":"pravin@1234gmail.com",
        "password" :"Pravin@1234"
        }
        
      this will generate access token output :
        {
        "token": "f0b26fa7d47820c968ed30608d58d6a793e3ec95"
        }
        
      note : we need to add token to headdres of POSTMAN API in this format
             Key : Authorization  Values : token f0b26fa7d47820c968ed30608d58d6a793e3ec95



3 >   To get list of all blog type http://127.0.0.1:8000/api/ with GET method it will produce this type of output :
      this output will have id of blog, title, content, author(owner of blog), published date, updated date, likes count
      output format : 
      [
        {
            "id": "16330829-7ee6-4a7e-847a-6049a10a2f9f",
            "title": "Where does it come from?",
            "content": "Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of \"de Finibus Bonorum et Malorum\" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, \"Lorem ipsum dolor sit amet..\", comes from a line in section 1.10.32.",
            "author": "pravin@gmail.com",
            "published_date": "2023-04-30T12:35:55.107946Z",
            "updated_date": "2023-04-30T12:40:29.977066Z",
            "likes": 3,
            "is_deleted": false
        },
        {
            "id": "1dccccbe-5611-4c5e-870a-5c1a08e9f369",
            "title": "Where can I get some?",
            "content": "There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc.",
            "author": "pravin123@gmail.com",
            "published_date": "2023-04-30T12:35:29.348829Z",
            "updated_date": "2023-04-30T12:40:23.306359Z",
            "likes": 4,
            "is_deleted": false
        },
        {
            "id": "2bf9dd7e-b559-47ce-b672-224b4ad2ac19",
            "title": "What is Lorem Ipsum?",
            "content": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum",
            "author": "pravin1222@gmail.com",
            "published_date": "2023-04-30T12:35:10.351539Z",
            "updated_date": "2023-04-30T12:40:18.481881Z",
            "likes": 2,
            "is_deleted": false
        },
        {
            "id": "57b58d09-a7e3-4b13-a08d-11fdd1ea039b",
            "title": "Why do we use it?",
            "content": "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).",
            "author": "pravin@gmail.com",
            "published_date": "2023-04-30T12:34:46.320092Z",
            "updated_date": "2023-04-30T12:40:13.830471Z",
            "likes": 2,
            "is_deleted": false
        }
    ]


4 >  To create new blog post we need to login first which will create authorization token and we need to add it to headders of API Postman Tester
      to create new blog go to  http://127.0.0.1:8000/api/   url and make   POST  request with this input format
      system will automatically create author to requested user
      
      input format to create new blog is :
        {"title":"here is your title of blog post",
        "content":" here is your actual blog content"
        }
    
      output format :
        {
        "status": "success",
        "details": "Successfully saved!",
        "data": {
            "id": "aaf101e6-3706-4f65-a268-249956c3f2b5",
            "title": "here is your title of blog post",
            "content": "here is your actual blog content",
            "author": "pravin123@gmail.com",
            "published_date": "2023-04-30T13:17:37.632133Z",
            "updated_date": "2023-04-30T13:17:37.632133Z",
            "likes": 0,
            "is_deleted": false
            }
        }


5 > To view a single blog in detail go to http://127.0.0.1:8000/api/detail/<slug:ID-OF BLOG>/  with GET method 
    EG : http://127.0.0.1:8000/api/detail/aaf101e6-3706-4f65-a268-249956c3f2b5/ 

    output :
        {
          "id": "aaf101e6-3706-4f65-a268-249956c3f2b5",
          "title": "here is your title of blog post",
          "content": "here is your actual blog content",
          "author": "pravin123@gmail.com",
          "published_date": "2023-04-30T13:17:37.632133Z",
          "updated_date": "2023-04-30T13:17:37.632133Z",
          "likes": 0,
          "is_deleted": false
        }

6 > To like Blog post we need to make POST METHOD request to this url http://127.0.0.1:8000/api/detail/<slug:ID-OF BLOG>/
    EG : http://127.0.0.1:8000/api/detail/aaf101e6-3706-4f65-a268-249956c3f2b5/ 
    
    this will add the current requested user to likes of that blog post
    output : 
      {
          "id": "aaf101e6-3706-4f65-a268-249956c3f2b5",
          "title": "here is your title of blog post",
          "content": "here is your actual blog content",
          "author": "pravin123@gmail.com",
          "published_date": "2023-04-30T13:17:37.632133Z",
          "updated_date": "2023-04-30T13:17:37.632133Z",
          "likes": 1,
          "is_deleted": false
        }
        
        
  Note : when user again make POST request this will remove current user from likes
  


7  > To make any changes to title or content of blog post make PUT request to this url http://127.0.0.1:8000/api/detail/<slug:ID-OF BLOG>/
      EG : http://127.0.0.1:8000/api/detail/aaf101e6-3706-4f65-a268-249956c3f2b5/ 
      
      note : changes are only allowed when requested user is author of blog post

      input format  :
                    {
                    "title":"here is your title of blog post",
                    "content":" here is your actual blog content"
                    }


      out format  :
                   {
                    "status": "success",
                    "details": "successfully updated",
                    "data": {
                        "id": "aaf101e6-3706-4f65-a268-249956c3f2b5",
                        "title": "here is your title of blog post",
                        "content": "here is your actual blog content",
                        "author": "pravin123@gmail.com",
                        "published_date": "2023-04-30T13:17:37.632133Z",
                        "updated_date": "2023-04-30T13:32:41.677403Z",
                        "likes": 1,
                        "is_deleted": false
                        }
                    }


8 > To delete blog post make DELETE request to this url http://127.0.0.1:8000/api/detail/<slug:ID-OF BLOG>/
      EG : http://127.0.0.1:8000/api/detail/aaf101e6-3706-4f65-a268-249956c3f2b5/ 

      note : Delete is only allowed when requested user is author of blog post
             this method dont need any input. only id which is passed to url is necessecory
      
      output format : 
              {
                "status": "success",
                "details": "successfully deleted post."
              }






9 > To view all comments of particular blog go to http://127.0.0.1:8000/api/comment/<slug:ID-OF BLOG>/   make a GET request
     EG : http://127.0.0.1:8000/api/comment/57b58d09-a7e3-4b13-a08d-11fdd1ea039b/

  thw field  replies are the reply to that comment 
  
  successfully implemented nested reples , comment module

  output:
           [
                {
                    "id": "3852b22b-9521-4723-a4e1-80c74255226b",
                    "blog": "57b58d09-a7e3-4b13-a08d-11fdd1ea039b",
                    "owner": "pravin@gmail.com",
                    "content": "very good blog",
                    "created_date": "2023-04-30T12:36:22.080940Z",
                    "replies": [
                        {
                            "id": "1df1a5fb-0867-49c9-ae01-73c943d1da41",
                            "blog": "57b58d09-a7e3-4b13-a08d-11fdd1ea039b",
                            "owner": "pravin12@gmail.com",
                            "content": "nicely done",
                            "created_date": "2023-04-30T12:36:37.693605Z",
                            "replies": [
                                {
                                    "id": "7b8b041b-2dff-46b3-8a0d-c4f44f6dd407",
                                    "blog": "57b58d09-a7e3-4b13-a08d-11fdd1ea039b",
                                    "owner": "pravin123@gmail.com",
                                    "content": "great job",
                                    "created_date": "2023-04-30T12:36:57.028933Z",
                                    "replies": []
                                }
                            ]
                        }
                    ]
                }
            ]
  
  


10  > to create new comment make POST request to http://127.0.0.1:8000/api/comment/<slug:ID-OF BLOG>/
    EG : http://127.0.0.1:8000/api/comment/57b58d09-a7e3-4b13-a08d-11fdd1ea039b/
    
    
    NOTE : 
          only authenticated user are allowed to create a new comment
          owner will be automatically assigned to requested user
          
    input format :  blog field will require id of blog post
                  
        { "blog":"57b58d09-a7e3-4b13-a08d-11fdd1ea039b",   
          "content":" here is your comment"
          }
          
     output format : 
            {
                  "status": "success",
                  "details": "successfully saved comment",
                  "data": {
                      "id": "2f6b2c1f-0620-42cb-ae76-0df4d406986b",
                      "blog": "57b58d09-a7e3-4b13-a08d-11fdd1ea039b",
                      "owner": "pravin123@gmail.com",
                      "content": "here is your comment",
                      "created_date": "2023-04-30T13:52:37.928906Z",
                      "replies": []
                  }
              }

    
    
11  > To reply any comment make PUT request to http://127.0.0.1:8000/api/comment/<slug:ID-OF BLOG>/
    EG : http://127.0.0.1:8000/api/comment/57b58d09-a7e3-4b13-a08d-11fdd1ea039b/
    
     NOTE : 
          only authenticated user are allowed to create a new comment
          owner will be automatically assigned to requested user
          
      input format  :
         {          "blog":"57b58d09-a7e3-4b13-a08d-11fdd1ea039b",
                    "content":" here is your comment",
                    "reply-to": "2f6b2c1f-0620-42cb-ae76-0df4d406986b"
          }
    
      output format : 
            {
                  "status": "success",
                  "details": "successfully updated",
                  "data": {
                      "id": "771a6de2-beba-4447-a832-2569b7124fb4",
                      "blog": "57b58d09-a7e3-4b13-a08d-11fdd1ea039b",
                      "owner": "pravin123@gmail.com",
                      "content": "here is your comment",
                      "created_date": "2023-04-30T13:56:39.805145Z",
                      "replies": []
                  }
              }

    
    
    
    
12  > To search a blog with keyword make POST request to  http://127.0.0.1:8000/api/search/
    NOTE : search will take keywords  and try to search it in title of each blog post and return the blog which matches to that keyword

  input formar : 
          {
              "search" :" Lorem"
          }

    
  output format :
              [
              {
                  "id": "2bf9dd7e-b559-47ce-b672-224b4ad2ac19",
                  "title": "What is Lorem Ipsum?",
                  "content": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum",
                  "author": "pravin1222@gmail.com",
                  "published_date": "2023-04-30T12:35:10.351539Z",
                  "updated_date": "2023-04-30T12:40:18.481881Z",
                  "likes": 2,
                  "is_deleted": false
              }
          ]



