# Project 2: Moonlight Museum After Dark

## Team information
- Team name: Moonlight Coders
- Members: Anu
- Repository name: project-2-moonlight-museum-after-dark-AnuuDumjan

---

## Project summary

Our project builds a system for organizing strange museum artifacts after dark.  
The system uses multiple data structures like BST, Queue, Stack, and Linked List to manage artifacts, restoration requests, exhibit routes, and reports.  
It helps museum staff search artifacts, process repairs, track actions, and manage visitor routes efficiently.

---

## Feature checklist

### Core structures
- [x] `Artifact` class/record
- [x] `ArtifactBST`
- [x] `RestorationQueue`
- [x] `ArchiveUndoStack`
- [x] `ExhibitRoute` singly linked list

### BST features
- [x] insert artifact
- [x] search by ID
- [x] preorder traversal
- [x] inorder traversal
- [x] postorder traversal
- [x] duplicate IDs ignored

### Queue features
- [x] add request
- [x] process next request
- [x] peek next request
- [x] empty check
- [x] size

### Stack features
- [x] push action
- [x] undo last action
- [x] peek last action
- [x] empty check
- [x] size

### Linked list features
- [x] add stop to end
- [x] remove first matching stop
- [x] list stops in order
- [x] count stops

### Utility/report features
- [x] category counts
- [x] unique rooms
- [x] sort by age
- [x] linear search by name

### Integration
- [x] `demo_museum_night()`
- [x] at least 8 artifacts in demo
- [x] demo shows system parts working together

---

## Design note (150-250 words)

We used a Binary Search Tree (BST) for artifact IDs because searching and inserting by ID becomes faster compared to a normal list. Since each artifact has a unique ID, BST helps keep them organized in sorted order.

A queue is used for restoration requests because restoration tasks should be processed in the same order they arrive. This follows the FIFO (First In First Out) rule, which is perfect for repair requests.

A stack is used for undo actions because the most recent action should be undone first. This follows the LIFO (Last In First Out) rule and makes undo operations simple and efficient.

A linked list is used for the exhibit route because stops can be added or removed easily without shifting all elements like in a normal list. It is useful for changing exhibit paths.

The system is divided into separate classes for each structure. BST handles artifacts, Queue manages restoration requests, Stack stores archive actions, and Linked List manages exhibit routes. Utility functions help create reports like counting categories, sorting by age, and searching by artifact name.

---

## Complexity reasoning

- `ArtifactBST.insert`: `O(h)` where h is the tree height because insertion follows one path from root to leaf.

- `ArtifactBST.search_by_id`: `O(h)` where h is the tree height because it checks only one branch at each step.

- `ArtifactBST.inorder_ids`: `O(n)` because every node is visited exactly once.

- `RestorationQueue.process_next_request`: `O(1)` because deque removes from the front in constant time.

- `ArchiveUndoStack.undo_last_action`: `O(1)` because list pop from the end is constant time.

- `ExhibitRoute.remove_stop`: `O(n)` because it may need to check every node in the linked list.

- `sort_artifacts_by_age`: `O(n log n)` because Python sorting uses efficient sorting algorithms.

- `linear_search_by_name`: `O(n)` because it checks artifacts one by one.

---

## Edge-case checklist

### BST
- [x] insert into empty tree
- [x] search for missing ID
- [x] empty traversals
- [x] duplicate ID

### Queue
- [x] process empty queue
- [x] peek empty queue

### Stack
- [x] undo empty stack
- [x] peek empty stack

### Exhibit route linked list
- [x] empty route
- [x] remove missing stop
- [x] remove first stop
- [x] remove middle stop
- [x] remove last stop
- [x] one-stop route

### Reports
- [x] empty artifact list
- [x] repeated categories
- [x] repeated rooms
- [x] missing artifact name
- [x] same-age artifacts

---

## Demo plan / how to run

```bash
pytest -q
python -c "from src.project import demo_museum_night; demo_museum_night()"