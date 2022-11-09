import os
import json

from PySide2 import QtCore, QtGui
from PySide2.QtWidgets import QApplication, QStyle, QStyleOptionButton

from mapclient.core.workflow.workflowsteps import addStep
from mapclient.view.workflow.workflowsteptreeview import HeaderDelegate
from mapclient.mountpoints.workflowstep import WorkflowStepMountPoint


class MAPPlugin:
    def __init__(self, name, category, icon_name, url):
        """
        This is a simplified version of the WorkflowSteps class, to be used for visualizing step objects that aren't installed locally.
        """
        self._name = name
        self._category = category
        self._icon = icon_name
        self._url = url

    def get_name(self):
        return self._name

    def get_category(self):
        return self._category

    def get_icon_name(self):
        return self._icon

    def get_url(self):
        return self._url

    def __iter__(self):
        yield from {
            "_name": self._name,
            "_category": self._category,
            "_icon": self._icon,
            "_url": self._url
        }.items()

    def __str__(self):
        return json.dumps(dict(self), ensure_ascii=False)

    def __repr__(self):
        return self.__str__()

    def to_json(self):
        return self.__dict__

    @staticmethod
    def from_json(json_dict):
        return MAPPlugin(json_dict['_name'], json_dict['_category'], json_dict['_icon'], json_dict['_url'])


# This makes the MAPPlugin class compatible with workflowsteps.addStep().
setattr(MAPPlugin, 'getName', MAPPlugin.get_name)


class PluginData(QtGui.QStandardItemModel):

    def __init__(self, plugins, parent=None):
        super(PluginData, self).__init__(parent)
        self._plugins = plugins

    def reload(self):
        self.clear()
        self.setColumnCount(1)
        for plugin in self._plugins.values():
            addStep(self, plugin)


class PushButtonDelegate(HeaderDelegate):
    buttonClicked = QtCore.Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self._pressed = None
        self._installed_plugins = self.get_installed_plugins()
        self._download_icon = QtGui.QPixmap(':/mapclient/images/download_icon.png')
        self._downloaded_icon = QtGui.QPixmap(':/mapclient/images/downloaded_icon.png')
        self._loading_icon = QtGui.QPixmap(':/mapclient/images/loading_icon.png')

    def paint(self, painter, option, index):
        super(PushButtonDelegate, self).paint(painter, option, index)

        if not index.parent().row() < 0:
            opt = QStyleOptionButton()

            name = index.data()
            if name in self._installed_plugins.keys():
                if self._installed_plugins[name]:
                    opt.icon = self._downloaded_icon
                else:
                    opt.icon = self._loading_icon
            else:
                opt.icon = self._download_icon

            opt.iconSize = QtCore.QSize(48, 48)
            opt.rect = self.get_button_rect(option)

            if self._pressed and self._pressed == (index.row(), index.column()):
                opt.state = QStyle.State_Enabled | QStyle.State_Sunken
            else:
                opt.state = QStyle.State_Enabled | QStyle.State_Raised
            QApplication.style().drawControl(QStyle.CE_PushButton, opt, painter)

    def editorEvent(self, event, model, option, index):
        if index.data() in self._installed_plugins.keys():
            return True

        if event.type() == QtCore.QEvent.MouseButtonPress:
            if self.get_button_rect(option).contains(event.pos()):
                self._pressed = (index.row(), index.column())
            return True

        elif event.type() == QtCore.QEvent.MouseButtonRelease:
            if self._pressed == (index.row(), index.column()):
                if self.get_button_rect(option).contains(event.pos()):
                    plugin = model.data(index, QtCore.Qt.UserRole + 1)
                    self.buttonClicked.emit(plugin.get_url())
            self._pressed = None
            return True

        return False

    @staticmethod
    def get_installed_plugins():
        installed_plugins = {}
        for step in WorkflowStepMountPoint.getPlugins(''):
            installed_plugins[step.getName()] = True

        return installed_plugins

    @staticmethod
    def get_button_rect(option):
        button_rect = option.rect
        button_rect.setRect(button_rect.width() - 58, button_rect.y() + 8, 48, 48)
        return button_rect


def get_step_database_file():
    return os.path.join(os.path.dirname(__file__), 'plugin_manager', 'plugin_database.json')


def read_step_database():
    database_file = get_step_database_file()

    try:
        with open(database_file, "r") as file:
            data = json.load(file, object_hook=from_json)
    except IOError:
        data = {}

    return data


def from_json(json_dict):
    if '_name' in json_dict.keys():
        return MAPPlugin.from_json(json_dict)
    else:
        return json_dict


def write_step_database(data):
    database_file = get_step_database_file()
    if not os.path.exists(os.path.dirname(database_file)):
        os.mkdir(os.path.dirname(database_file))

    with open(database_file, "w") as file:
        json.dump(data, file, default=default)


def read_step_info(step_file):
    def read_value(identifier):
        value = read_line(line, identifier)
        if not value:
            extended_line = line + next(lines).strip(' \t\r\n')
            value = read_line(extended_line, identifier)

        return value

    name = category = icon_path = None
    lines = iter(step_file.splitlines())
    for line in lines:
        line = line.strip()

        if line.startswith("super"):
            name = read_value("__init__")
        elif line.startswith("self._category"):
            category = read_value("=")
            if icon_path:
                break
        elif line.startswith("self._icon"):
            icon_path = read_value("QImage")
            if category:
                break

    return name, category, icon_path


def read_line(line, identifier):

    value = None
    for quote in ["'", '"']:
        start = line.find(quote, line.find(identifier) + len(identifier))
        if start == -1:
            continue
        end = line.find(quote, start + 1)
        value = line[start:end].strip(' "\'\t\r\n')

    return value


def get_icon(plugin):
    icon_path = os.path.join(os.path.dirname(__file__), 'plugin_manager', 'icons', plugin['icon_name'])

    return QtGui.QImage(icon_path)


def save_plugin_icon(icon_path):
    save_dir = os.path.join(os.path.dirname(__file__), 'plugin_manager', 'icons')

    # TODO: Implement.
    icon_name = ""

    return icon_name


def default(obj):
    if hasattr(obj, 'to_json'):
        return obj.to_json()
    raise TypeError(f'Object of type {obj.__class__.__name__} is not JSON serializable')
