# CoderSchool FTW - _ Github Issue Project _

Created with love by: `Nguyen Vu`


## Video Walkthrough

Here's a walkthrough of implemented user stories.

To create a GIF, use [LiceCap](http://www.cockos.com/licecap/), [RecordIt](http://www.recordit.co), or [Loom](http://www.useloom.com), and link the image here in the markdown.

```
<img src='http://i.imgur.com/link/to/your/gif/file.gif' title='Video Walkthrough' width='' alt='Video Walkthrough' />
```

## Required Features 🎯
- [x]User can run app program from command line.
- [x]User can see all todos from the command line by passing a list command, sorted by due todos first.
- [x]User can add a todo from the command line by passing an argument, add. The fields specified should be body, due_date, and project_id. The fields due_date and project_id are optional. Only body is required.
- [x]By default todos are incomplete.
- [x]User should see a message giving information about the todo that was added.
- [x]User can mark a todo as complete by passing a command and an id.
- [x]User can mark a todo as incomplete by passing a command and an id.
- [x]If the user does not supply the correct arguments, or supplies a --help flag, the user sees a usage message.
- [x]The user can supply arguments to the list command to only see todos that are complete.
- [x]Project has a ERD Diagram in it's README.md.
## Rockets 🚀
- [x]User can use the app as a R.E.P.L.
- [x]User can supply arguments to the list command to only see todos of a particular project_id.
- [x]User can supply arguments to the list command to reverse the default sort, to now see the todos by due_date descending.
- []User can supply arguments to the list command to combine the above options.
- [x]User can add a user_id to each todo.
- [x]User can add a user to the system by passing add_user. Each user should have a name, email_address, and id.
- [x]User can call a list_users command that shows all the users in the system.
- [x]User can call a staff command that shows each project, combined with each of the users working on that project.
- [_]User can call a who_to_fire command that lists all users who are not currently assigned a todo.
- [_]User can add a project by calling add_project. Each project must have a name.
- [_]User can see all projects from the command line.


## License

    Copyright [p-todos] [Nguyen Vu]

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
