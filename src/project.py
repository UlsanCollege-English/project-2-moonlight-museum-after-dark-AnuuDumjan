"""Project 2 starter code: Moonlight Museum After Dark.

Students should implement all required behavior in this file.
Use stdlib only.
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from typing import Deque


@dataclass(frozen=True)
class Artifact:
    """A museum artifact stored in the archive BST."""

    artifact_id: int
    name: str
    category: str
    age: int
    room: str


@dataclass(frozen=True)
class RestorationRequest:
    """A request to inspect or repair an artifact."""

    artifact_id: int
    description: str


class TreeNode:
    """A node for the artifact BST."""

    def __init__(
        self,
        artifact: Artifact,
        left: TreeNode | None = None,
        right: TreeNode | None = None,
    ) -> None:
        self.artifact = artifact
        self.left = left
        self.right = right


class ArtifactBST:
    """Binary search tree keyed by artifact_id."""

    def __init__(self) -> None:
        self.root: TreeNode | None = None

    def insert(self, artifact: Artifact) -> bool:
        if self.root is None:
            self.root = TreeNode(artifact)
            return True

        current = self.root

        while True:
            if artifact.artifact_id == current.artifact.artifact_id:
                return False

            elif artifact.artifact_id < current.artifact.artifact_id:
                if current.left is None:
                    current.left = TreeNode(artifact)
                    return True
                current = current.left

            else:
                if current.right is None:
                    current.right = TreeNode(artifact)
                    return True
                current = current.right

    def search_by_id(self, artifact_id: int) -> Artifact | None:
        current = self.root

        while current is not None:
            if artifact_id == current.artifact.artifact_id:
                return current.artifact
            elif artifact_id < current.artifact.artifact_id:
                current = current.left
            else:
                current = current.right

        return None

    def inorder_ids(self) -> list[int]:
        result = []

        def traverse(node):
            if node is not None:
                traverse(node.left)
                result.append(node.artifact.artifact_id)
                traverse(node.right)

        traverse(self.root)
        return result

    def preorder_ids(self) -> list[int]:
        result = []

        def traverse(node):
            if node is not None:
                result.append(node.artifact.artifact_id)
                traverse(node.left)
                traverse(node.right)

        traverse(self.root)
        return result

    def postorder_ids(self) -> list[int]:
        result = []

        def traverse(node):
            if node is not None:
                traverse(node.left)
                traverse(node.right)
                result.append(node.artifact.artifact_id)

        traverse(self.root)
        return result


class RestorationQueue:
    """FIFO queue of restoration requests."""

    def __init__(self) -> None:
        self._items: Deque[RestorationRequest] = deque()

    def add_request(self, request: RestorationRequest) -> None:
        self._items.append(request)

    def process_next_request(self) -> RestorationRequest | None:
        if self._items:
            return self._items.popleft()
        return None

    def peek_next_request(self) -> RestorationRequest | None:
        if self._items:
            return self._items[0]
        return None

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def size(self) -> int:
        return len(self._items)


class ArchiveUndoStack:
    """LIFO stack of recent archive actions."""

    def __init__(self) -> None:
        self._items: list[str] = []

    def push_action(self, action: str) -> None:
        self._items.append(action)

    def undo_last_action(self) -> str | None:
        if self._items:
            return self._items.pop()
        return None

    def peek_last_action(self) -> str | None:
        if self._items:
            return self._items[-1]
        return None

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def size(self) -> int:
        return len(self._items)


class ExhibitNode:
    """A node in the singly linked exhibit route."""

    def __init__(self, stop_name: str, next_node: ExhibitNode | None = None) -> None:
        self.stop_name = stop_name
        self.next = next_node


class ExhibitRoute:
    """Singly linked list of exhibit stops."""

    def __init__(self) -> None:
        self.head: ExhibitNode | None = None

    def add_stop(self, stop_name: str) -> None:
        new_node = ExhibitNode(stop_name)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node

    def remove_stop(self, stop_name: str) -> bool:
        current = self.head
        previous = None

        while current is not None:
            if current.stop_name == stop_name:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                return True

            previous = current
            current = current.next

        return False

    def list_stops(self) -> list[str]:
        result = []
        current = self.head

        while current is not None:
            result.append(current.stop_name)
            current = current.next

        return result

    def count_stops(self) -> int:
        count = 0
        current = self.head

        while current is not None:
            count += 1
            current = current.next

        return count


def count_artifacts_by_category(artifacts: list[Artifact]) -> dict[str, int]:
    result = {}

    for artifact in artifacts:
        if artifact.category in result:
            result[artifact.category] += 1
        else:
            result[artifact.category] = 1

    return result


def unique_rooms(artifacts: list[Artifact]) -> set[str]:
    rooms = set()

    for artifact in artifacts:
        rooms.add(artifact.room)

    return rooms


def sort_artifacts_by_age(
    artifacts: list[Artifact],
    descending: bool = False,
) -> list[Artifact]:
    return sorted(artifacts, key=lambda x: x.age, reverse=descending)


def linear_search_by_name(
    artifacts: list[Artifact],
    name: str,
) -> Artifact | None:
    for artifact in artifacts:
        if artifact.name == name:
            return artifact

    return None


def demo_museum_night() -> None:
    print("Moonlight Museum After Dark")

    bst = ArtifactBST()

    artifacts = [
        Artifact(10, "Mask", "History", 200, "Room A"),
        Artifact(5, "Vase", "Ceramic", 150, "Room B"),
        Artifact(15, "Sword", "Weapon", 300, "Room C"),
        Artifact(3, "Coin", "Ancient", 500, "Room D"),
        Artifact(7, "Statue", "Art", 250, "Room E"),
        Artifact(12, "Painting", "Art", 100, "Room F"),
        Artifact(18, "Helmet", "Armor", 350, "Room G"),
        Artifact(20, "Shield", "Armor", 400, "Room H"),
    ]

    for artifact in artifacts:
        bst.insert(artifact)

    print("Inorder IDs:", bst.inorder_ids())

    queue = RestorationQueue()
    queue.add_request(RestorationRequest(10, "Fix cracks"))
    print("Next restoration request:", queue.peek_next_request())

    stack = ArchiveUndoStack()
    stack.push_action("Added artifact")
    print("Undo action:", stack.peek_last_action())

    route = ExhibitRoute()
    route.add_stop("Entrance Hall")
    route.add_stop("Ancient Gallery")
    print("Exhibit route:", route.list_stops())

    print("Category counts:", count_artifacts_by_category(artifacts))