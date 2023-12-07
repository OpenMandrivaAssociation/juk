Summary:	A music player and manager for KDE
Name:		juk
Version:	23.08.4
Release:	1
Epoch:		3
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org/applications/multimedia/juk/
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(taglib) >= 1.7
BuildRequires:	ninja
BuildRequires:	appstream
BuildRequires:	cmake
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5Completion)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5Crash)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5GlobalAccel)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5JobWidgets)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5TextWidgets)
BuildRequires:	cmake(KF5Wallet)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5WindowSystem)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(Phonon4Qt5)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5DBus)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Network)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Xml)

# Tunepimp support hasn't been ported to KDE5
BuildConflicts:	libtunepimp-devel

%description
JuK is an audio jukebox application, supporting collections of MP3, Ogg
Vorbis, and FLAC audio files. It allows you to edit the "tags" of your
audio files, and manage your collection and playlists. It's main focus,
in fact, is on music management.

%files -f juk.lang
%{_bindir}/juk
%{_datadir}/kxmlgui5/juk
%{_datadir}/icons/*/*/*/*.*
%{_datadir}/metainfo/*.xml
%{_datadir}/applications/org.kde.juk.desktop
%{_datadir}/dbus-1/interfaces/org.kde.juk.*.xml
%{_datadir}/juk
%{_datadir}/knotifications5/juk.notifyrc
%{_datadir}/kio/servicemenus/jukservicemenu.desktop

#------------------------------------------------------------------------------

%prep
%autosetup -p1
%cmake_kde5

%build
ninja -C build

%install
%ninja_install -C build
%find_lang juk --all-name --with-html
