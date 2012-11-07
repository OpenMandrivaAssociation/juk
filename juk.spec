Name:		juk
Version: 4.9.3
Release: 1
Epoch:		3
Summary:	A music player and manager for KDE
Group:		Graphical desktop/KDE
License:	GPLv2
URL:		http://www.kde.org/applications/multimedia/juk/
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
Requires:	kdebase4-runtime
Conflicts:	kdemultimedia4-core < 3:4.5.71
Conflicts:	kdemultimedia4-devel < 3:4.6.90-3
BuildRequires:	kdelibs4-devel
BuildRequires:	libtunepimp-devel
BuildRequires:	pkgconfig(taglib) >= 1.7

%description
JuK is an audio jukebox application, supporting collections of MP3, Ogg
Vorbis, and FLAC audio files. It allows you to edit the "tags" of your
audio files, and manage your collection and playlists. It's main focus,
in fact, is on music management.

%files
%{_kde_appsdir}/juk
%{_kde_bindir}/juk
%{_kde_iconsdir}/*/*/apps/juk.*
%{_kde_applicationsdir}/juk.desktop
%{_kde_services}/ServiceMenus/jukservicemenu.desktop
%{_datadir}/dbus-1/interfaces/org.kde.juk.collection.xml
%{_datadir}/dbus-1/interfaces/org.kde.juk.player.xml
%{_datadir}/dbus-1/interfaces/org.kde.juk.search.xml
%{_kde_docdir}/HTML/en/juk

#------------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

