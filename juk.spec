Summary:	A music player and manager for KDE
Name:		juk
Version:	15.12.3
Release:	2
Epoch:		3
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org/applications/multimedia/juk/
Source0:	http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	libtunepimp-devel
BuildRequires:	kdelibs-devel
BuildRequires:	pkgconfig(taglib) >= 1.7
Requires:	kde-runtime

%description
JuK is an audio jukebox application, supporting collections of MP3, Ogg
Vorbis, and FLAC audio files. It allows you to edit the "tags" of your
audio files, and manage your collection and playlists. It's main focus,
in fact, is on music management.

%files
%doc %{_kde_docdir}/HTML/en/juk
%{_kde_applicationsdir}/juk.desktop
%{_kde_appsdir}/juk
%{_kde_bindir}/juk
%{_kde_datadir}/appdata/juk.appdata.xml
%{_kde_iconsdir}/*/*/apps/juk.*
%{_kde_services}/ServiceMenus/jukservicemenu.desktop
%{_datadir}/dbus-1/interfaces/org.kde.juk.collection.xml
%{_datadir}/dbus-1/interfaces/org.kde.juk.player.xml
%{_datadir}/dbus-1/interfaces/org.kde.juk.search.xml

#------------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4 -DCMAKE_MINIMUM_REQUIRED_VERSION=2.6
%make

%install
%makeinstall_std -C build
